import pygame,assets,math,random
from classes.json_handler import JSON_handler
from classes.blocks import *
from classes.graph import Graph,Node
from classes.transition import transition_2bounds


def closest_rect(rect, rect_list):

    closest_rect = rect_list.pop(0)
    closest_distance = math.sqrt((rect.centerx - closest_rect.centerx) ** 2 + (rect.centery - closest_rect.centery) ** 2)

    for r in rect_list:
        distance = math.sqrt((rect.centerx - r.centerx) ** 2 + (rect.centery - r.centery) ** 2)
        if distance < closest_distance:
            closest_distance = distance
            closest_rect = r

    return closest_rect


class Game_map(pygame.sprite.Sprite):

    def __init__(
        self,
        winsize,
        loc,
        size,
        lvl_path,
        parent_groups,
        layer = 0,
        living = True,
    ):

        super().__init__()

        
        ratio = winsize[0] / assets.DEFAULT_WINSIZE[0]

        self._layer = layer
        self.pos = [i*ratio for i in loc[0]]
        self.placement_mode = loc[1]
        self.lvl_path = lvl_path
        self.parent_groups = parent_groups
        self.save_manager = JSON_handler()
        self.save_manager.read(lvl_path)
        matrix = self.save_manager["matrix"]

        self.group = pygame.sprite.LayeredUpdates()
        self.x_cells = len(matrix[0:matrix.find("\n")])
        self.y_cells = matrix.count("\n")
        matrix = matrix.replace("\n","")
        self.cell_width = (min(size[0] / self.x_cells, size[1] / self.y_cells))*ratio
        self.cell_width = round(self.cell_width) + round(self.cell_width) % 2
        self.cells = []
        i = 0
        for y in range(self.y_cells):
            temp_cells = []
            for x in range(self.x_cells):
                if matrix[i] in ["X","■"]:
                    temp_cells.append(Wall(
                        winsize = winsize,
                        topleft = [x*self.cell_width,y*self.cell_width],
                        width = self.cell_width,
                        group = self.group))
                elif matrix[i] == "_":
                    temp_cells.append(Ghost_door(
                        winsize = winsize,
                        topleft = [x*self.cell_width,y*self.cell_width],
                        width = self.cell_width,
                        group = self.group))
                elif matrix[i] == "P":
                    self.pacman = Pacman(
                        winsize = winsize,
                        topleft = [x*self.cell_width,y*self.cell_width],
                        width = self.cell_width,
                        group = self.group,
                        game_map = self)
                    temp_cells.append(Empty_cell(
                        winsize = winsize,
                        topleft = [x*self.cell_width,y*self.cell_width],
                        width = self.cell_width,
                        group = self.group))
                elif matrix[i] == ".":
                    temp_cells.append(Coin(
                        winsize = winsize,
                        topleft = [x*self.cell_width,y*self.cell_width],
                        width = self.cell_width,
                        group = self.group))
                elif matrix[i] == "●":
                    temp_cells.append(Super_coin(
                        winsize = winsize,
                        topleft = [x*self.cell_width,y*self.cell_width],
                        width = self.cell_width,
                        group = self.group))
                else:
                    temp_cells.append(Empty_cell(
                        winsize = winsize,
                        topleft = [x*self.cell_width,y*self.cell_width],
                        width = self.cell_width,
                        group = self.group))
                i+=1
            self.cells.append(temp_cells)

        x,y = self.x_cells//2, self.y_cells//2
        locs = [[(x-1)*self.cell_width,(y-1)*self.cell_width],
        [(x+1)*self.cell_width,(y-1)*self.cell_width],
        [(x-1)*self.cell_width,y*self.cell_width],
        [(x+1)*self.cell_width,y*self.cell_width]]
        self.ghosts = []
        for i in range(self.save_manager["nb_ghosts"]):
            self.ghosts.append(Ghost(
                winsize = winsize,
                topleft = random.choice(locs),
                color = assets.GHOST_COLORS[i],
                width = self.cell_width,
                group = self.group,
                game_map = self,
                speed = transition_2bounds(3,5,self.save_manager["nb_ghosts"],'linear',i)
            ))
        [(x-1)*self.cell_width,(y-1)*self.cell_width]
        [(x+1)*self.cell_width,(y-1)*self.cell_width]
        [(x-1)*self.cell_width,y*self.cell_width]
        [(x+1)*self.cell_width,y*self.cell_width]

        self.link_neighbors()
        self.generate_graph()
        if living:
            self.liven()

        self.calc_image()
        self.calc_rect()

    def liven(self):
        """
        A l'inverse de kill() (méthode de pygame.sprite.Sprite permettant de suppprimer le sprite de tous les groupes dans lesquels il se trouve), ajoute le sprite à tous ses groupes parents.
        """

        for group in self.parent_groups:
            group.add(self)


    def calc_image(self):

        self.image = pygame.Surface([self.x_cells*self.cell_width,self.y_cells*self.cell_width],pygame.SRCALPHA)
        self.group.draw(self.image)

    
    def calc_rect(self):

        pos = [round(i) for i in self.pos]
        if self.placement_mode == "topleft":
            self.rect = self.image.get_rect(topleft=pos)
        elif self.placement_mode == "topright":
            self.rect = self.image.get_rect(topright=pos)
        elif self.placement_mode == "bottomleft":
            self.rect = self.image.get_rect(bottomleft=pos)
        elif self.placement_mode == "bottomright":
            self.rect = self.image.get_rect(bottomright=pos)
        elif self.placement_mode == "midtop":
            self.rect = self.image.get_rect(midtop=pos)
        elif self.placement_mode == "midleft":
            self.rect = self.image.get_rect(midleft=pos)
        elif self.placement_mode == "midbottom":
            self.rect = self.image.get_rect(midbottom=pos)
        elif self.placement_mode == "midright":
            self.rect = self.image.get_rect(midright=pos)
        elif self.placement_mode == "center":
            self.rect = self.image.get_rect(center=pos)


    def update(self,new_winsize,dt,cursor):
        """Actualisation du sprite ayant lieu à chaque changement image"""

        self.pacman.update(dt)
        a = self.locate_pos(self.pacman.rect.center)
        # print(self.get_moves(self.graph.dijkstra([1,1],a)))
        
        colliding_cells = pygame.sprite.spritecollide(self.pacman,self.group,False)
        
        to_draw = []
        for sprite in colliding_cells:
            if type(sprite) not in [Ghost,Pacman]:
                for neighbor in list(sprite.next.values()) + [sprite]:
                    if neighbor is not None:
                        to_draw.append(neighbor)
        for cell in list(set(to_draw)):
            if cell is not None:
                self.draw_cell(cell)
        self.image.blit(self.pacman.image,self.pacman.rect)
        for ghost in self.ghosts:
            self.image.blit(ghost.image,ghost.rect)


    def draw_cell(self,cell):

        pygame.draw.rect(self.image,[0,0,0,0],cell.rect)
        self.image.blit(cell.image,cell.rect)


    def link_neighbors(self):
        for y in range(self.y_cells):
            for x in range(self.x_cells):
                cell = self.cells[y][x]
                y_top = y - 1
                y_bottom = y + 1
                x_left = x - 1
                x_right = x + 1
                if y_top >= 0:
                    cell.next["top"] = self.cells[y_top][x]
                if y_bottom < self.y_cells:
                    cell.next["bottom"] = self.cells[y_bottom][x]
                if x_left >= 0:
                    cell.next["left"] = self.cells[y][x_left]
                if x_right < self.x_cells:
                    cell.next["right"] = self.cells[y][x_right]


    def handle_input(self, dir):

        if self.pacman.direction is None:
            self.pacman.set_direction(dir)
        elif self.pacman.direction in ["right","left"]:
            if dir == "left":
                self.pacman.set_direction("left")
                self.pacman.next_direction = None
            elif dir == "right":
                self.pacman.set_direction("right")
                self.pacman.next_direction = None
            elif dir == "top":
                self.pacman.next_direction = "top"
            elif dir == "bottom":
                self.pacman.next_direction = "bottom"
        elif self.pacman.direction in ["top","bottom"]:
            if dir == "left":
                self.pacman.next_direction = "left"
            elif dir == "right":
                self.pacman.next_direction = "right"
            elif dir == "top":
                self.pacman.set_direction("top")
                self.pacman.next_direction = None
            elif dir == "bottom":
                self.pacman.set_direction("bottom")
                self.pacman.next_direction = None


    def search_cell(self,cell):
        """
        Recherche naïve d'une cellule dans la matrice de l'objet.
        """
        for y in range(self.y_cells):
            for x in range(self.x_cells):
                if cell is self.cells[y][x]:
                    return [y,x]
                

    def locate_cell(self,abs_pos):

        x,y = self.locate_pos(abs_pos)
        return self.cells[y][x]


    def locate_pos(self,abs_pos):

        y,x = abs_pos[1]//self.cell_width,abs_pos[0]//self.cell_width
        if y >= self.y_cells:
            y = self.y_cells-1
        if x >= self.x_cells:
            x = self.x_cells-1
        
        return  [int(x),int(y)]


    def generate_graph(self):

        self.graph = Graph(self)
        for y in range(self.y_cells):
            for x in range(self.x_cells):
                cell = self.cells[y][x]
                if type(cell) in [Empty_cell,Coin,Super_coin,Ghost_door]:
                    next = {}
                    for side,c in cell.next.items():
                        next[side] =  type(c) in [Empty_cell,Coin,Super_coin,Ghost_door]
                    nb_cells = list(next.values()).count(True)
                    if nb_cells == 4 or nb_cells == 3:
                        self.graph.add_node(Node([x,y]))
                    elif nb_cells == 2:
                        if (next["top"] and next["left"]) or (next["left"] and next["bottom"]) or (next["top"] and next["right"]) or (next["bottom"] and next["right"]):
                            self.graph.add_node(Node([x,y]))
        left_portals = []
        right_portals = []
        for y in range(self.y_cells):
            if type(self.cells[y][0]) is Empty_cell:
                left_node = Node([0,y])
                right_node = Node([self.x_cells-1,y])
                left_portals.append(left_node)
                self.graph.add_node(left_node)
                right_portals.append(right_node)
                self.graph.add_node(right_node)

        
        for node in self.graph.nodes.values():
            top = self.graph.nearest_node(node.pos,"top")
            bottom = self.graph.nearest_node(node.pos,"bottom")
            left = self.graph.nearest_node(node.pos,"left")
            right = self.graph.nearest_node(node.pos,"right")
            if top:
                self.graph.add_edge(node,top)
                self.graph.add_edge(top,node)
            if bottom:
                self.graph.add_edge(node,bottom)
                self.graph.add_edge(bottom,node)
            if left:
                self.graph.add_edge(node,left)
                self.graph.add_edge(left,node)
            if right:
                self.graph.add_edge(node,right)
                self.graph.add_edge(right,node)

        for left,right in zip(left_portals,right_portals):
            left.next["left"] = [right,1]
            right.next["right"] = [left,1]


    def get_moves(self,coords):

        directions = []

        for i in range(len(coords) - 1):
            x1, y1 = coords[i]
            x2, y2 = coords[i + 1]
            if y2 < y1:
                directions.append("top")
            elif y2 > y1:
                directions.append("bottom")
            elif x2 < x1:
                if x2 == 0 and x1 == self.x_cells-1:
                    directions.append("right")
                else:
                    directions.append("left")
            elif x2 > x1:
                if x1 == 0 and x2 == self.x_cells-1:
                    directions.append("left")
                else:
                    directions.append("right")
        return directions