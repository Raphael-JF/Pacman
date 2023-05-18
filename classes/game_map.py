import pygame,os,assets,math
from classes.json_handler import JSON_handler
from classes.blocks import *


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

        
        self.winsize = winsize
        self._layer = layer
        self.pos = list(loc[0])
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
        self.cell_width = min(size[0] / self.x_cells, size[1] / self.y_cells)
        self.cells = []
        i = 0
        cell_width = round(self.cell_width) + round(self.cell_width) % 2
        for y in range(self.y_cells):
            temp_cells = []
            for x in range(self.x_cells):
                if matrix[i] in ["X","■"]:
                    temp_cells.append(Wall(
                        winsize = self.winsize,
                        topleft = [x*cell_width,y*cell_width],
                        width = cell_width,
                        group = self.group))
                elif matrix[i] == "_":
                    temp_cells.append(Ghost_door(
                        winsize = self.winsize,
                        topleft = [x*cell_width,y*cell_width],
                        width = cell_width,
                        group = self.group))
                elif matrix[i] == "P":
                    self.pacman = Pacman(
                        winsize = self.winsize,
                        topleft = [x*cell_width,y*cell_width],
                        width = cell_width,
                        group = self.group)
                    temp_cells.append(Empty_cell(
                        winsize = self.winsize,
                        topleft = [x*cell_width,y*cell_width],
                        width = cell_width,
                        group = self.group))
                elif matrix[i] == ".":
                    temp_cells.append(Coin(
                        winsize = self.winsize,
                        topleft = [x*cell_width,y*cell_width],
                        width = cell_width,
                        group = self.group))
                elif matrix[i] == "●":
                    temp_cells.append(Super_coin(
                        winsize = self.winsize,
                        topleft = [x*cell_width,y*cell_width],
                        width = cell_width,
                        group = self.group))
                else:
                    temp_cells.append(Empty_cell(
                        winsize = self.winsize,
                        topleft = [x*cell_width,y*cell_width],
                        width = cell_width,
                        group = self.group))
                i+=1
            self.cells.append(temp_cells)
        self.link_neighbors()
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

        cell_width = round(self.cell_width) + round(self.cell_width) % 2
        self.image = pygame.Surface([self.x_cells*cell_width,self.y_cells*cell_width],pygame.SRCALPHA)
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

        if self.winsize != new_winsize:
            self.rescale(new_winsize)

        self.pacman.update(dt)

        if self.pacman.direction is not None:
            old_pacman_rect = self.pacman.rect
            self.pacman.rect = self.pacman.get_next_rect(dt)
            self.pacman_path(old_pacman_rect)
            self.check_walls()
        
        colliding_cells = pygame.sprite.spritecollide(self.pacman,self.group,False)
        if self.pacman in colliding_cells:
            colliding_cells.remove(self.pacman)
        to_draw = []
        for sprite in colliding_cells:
            for neighbor in list(sprite.next.values()) + [sprite]:
                if neighbor is not None:
                    to_draw.append(neighbor)
        for cell in list(set(to_draw)):
            if cell is not None:
                self.draw_cell(cell)
        self.image.blit(self.pacman.image,self.pacman.rect)


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

    def rescale(self,new_winsize):
        
        old_winsize = self.winsize[:]
        self.winsize = new_winsize
        self.ratio = self.winsize[0] / old_winsize[0]
        self.pos = [i*self.ratio for i in self.pos]
        self.cell_width *= self.ratio
        
        cell_width = round(self.cell_width) + round(self.cell_width) % 2
        new_cells = []
        for y in range(self.y_cells):
            temp_cells = []
            for x in range(self.x_cells):
                cell = self.cells[y][x]
                if isinstance(cell,Wall):
                    temp_cells.append(Wall(
                        winsize = self.winsize,
                        topleft = [x*cell_width,y*cell_width],
                        width = cell_width,
                        group = self.group))
                elif isinstance(cell,Ghost_door):
                    temp_cells.append(Ghost_door(
                        winsize = self.winsize,
                        topleft = [x*cell_width,y*cell_width],
                        width = cell_width,
                        group = self.group))
                elif isinstance(cell,Empty_cell):
                    temp_cells.append(Empty_cell(
                        winsize = self.winsize,
                        topleft = [x*cell_width,y*cell_width],
                        width = cell_width,
                        group = self.group))
                elif isinstance(cell,Coin):
                    temp_cells.append(Coin(
                        winsize = self.winsize,
                        topleft = [x*cell_width,y*cell_width],
                        width = cell_width,
                        group = self.group))
                elif isinstance(cell,Super_coin):
                    temp_cells.append(Super_coin(
                        winsize = self.winsize,
                        topleft = [x*cell_width,y*cell_width],
                        width = cell_width,
                        group = self.group))
                cell.kill()
            new_cells.append(temp_cells)

        self.cells = new_cells[:]
        self.link_neighbors()

        self.pacman.kill()
        pacman_pos = [i*self.ratio for i in self.pacman.pos]
        sprites = self.group.sprites()
        adjacent_rects= []
        for sprite in sprites:
            if isinstance(sprite,Empty_cell):
                matrix = self.save_manager["matrix"].replace("\n","")
                y,x = self.search_cell(sprite)
                if matrix[y*self.x_cells + x] in ["□","P"]:
                    adjacent_rects.append(sprite.rect)
        pacman_pos = closest_rect(self.pacman.rect,adjacent_rects).topleft
        self.pacman = Pacman(
            self.winsize,
            topleft = pacman_pos,
            width = cell_width,
            group = self.group
        )
        self.calc_image()
        self.calc_rect()
    
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
                

    def locate_cell(self,pos):

        cell_width = round(self.cell_width) + round(self.cell_width) % 2
        y,x = pos[1]//cell_width,pos[0]//cell_width
        if y >= self.y_cells:
            y = self.y_cells-1
        if x >= self.x_cells:
            x = self.x_cells-1

        return self.cells[int(y)][int(x)]
    

    def pacman_path(self,old_pacman_rect):

        if self.pacman.next_direction is not None:
            cell_width = round(self.cell_width) + round(self.cell_width) % 2
            if self.pacman.direction == "top":
                old_top = old_pacman_rect.top
                new_top = self.pacman.rect.top
                fixed_y = old_top - old_top%cell_width
                if old_top  >= fixed_y >=  new_top and type(self.locate_cell(self.pacman.rect.center).next[self.pacman.next_direction]) in [Coin,Super_coin,Empty_cell]:
                    self.pacman.rect.top = fixed_y
                    if self.pacman.next_direction == "left":
                        self.pacman.rect.centerx -= old_top - new_top
                    else:
                        self.pacman.rect.centerx += old_top - new_top
                    self.pacman.set_direction(self.pacman.next_direction)
                    self.pacman.next_direction = None

            elif self.pacman.direction == "bottom":
                old_bottom = old_pacman_rect.bottom
                new_bottom = self.pacman.rect.bottom
                fixed_y = old_bottom+cell_width-old_bottom%cell_width
                if old_bottom  <= fixed_y <=  new_bottom and type(self.locate_cell(self.pacman.rect.center).next[self.pacman.next_direction]) in [Coin,Super_coin,Empty_cell]:
                    self.pacman.rect.bottom = fixed_y
                    if self.pacman.next_direction == "left":
                        self.pacman.rect.centerx -= new_bottom - old_bottom
                    else:
                        self.pacman.rect.centerx += new_bottom - old_bottom
                    self.pacman.set_direction(self.pacman.next_direction)
                    self.pacman.next_direction = None

            elif self.pacman.direction == "left":
                old_left = old_pacman_rect.left
                new_left = self.pacman.rect.left
                fixed_x = old_left - old_left%cell_width
                if old_left  >= fixed_x >=  new_left and type(self.locate_cell(self.pacman.rect.center).next[self.pacman.next_direction]) in [Coin,Super_coin,Empty_cell]:
                    self.pacman.rect.left = fixed_x
                    if self.pacman.next_direction == "top":
                        self.pacman.rect.centery -= old_left - new_left
                    else:
                        self.pacman.rect.centery += old_left - new_left
                    self.pacman.set_direction(self.pacman.next_direction)
                    self.pacman.next_direction = None

            elif self.pacman.direction == "right":
                old_right = old_pacman_rect.right
                new_right = self.pacman.rect.right
                fixed_x = old_right+cell_width-old_right%cell_width
                if old_right  <= fixed_x <=  new_right and type(self.locate_cell(self.pacman.rect.center).next[self.pacman.next_direction]) in [Coin,Super_coin,Empty_cell]:
                    self.pacman.rect.right = fixed_x
                    if self.pacman.next_direction == "top":
                        self.pacman.rect.centery -= new_right - old_right
                    else:
                        self.pacman.rect.centery += new_right - old_right
                    self.pacman.set_direction(self.pacman.next_direction)
                    self.pacman.next_direction = None

    def check_walls(self):

        colliding = pygame.sprite.spritecollide(self.pacman,self.group,False,lambda a,b :a.rect.colliderect(b.rect))
        walls = [sprite for sprite in colliding if isinstance(sprite, Wall) or isinstance(sprite,Ghost_door)]
        if walls:
            wall = walls[0]
            if self.pacman.direction == "top" and self.pacman.rect.top <= wall.rect.bottom:
                self.pacman.rect.top = wall.rect.bottom
            elif self.pacman.direction == "bottom" and self.pacman.rect.bottom >= wall.rect.top:
                self.pacman.rect.bottom = wall.rect.top
            elif self.pacman.direction == "left" and self.pacman.rect.left <= wall.rect.right:
                self.pacman.rect.left = wall.rect.right
            elif self.pacman.direction == "right" and self.pacman.rect.right >= wall.rect.left:
                self.pacman.rect.right = wall.rect.left
            self.pacman.direction = None
            self.pacman.next_direction = None

        cell_width = round(self.cell_width) + round(self.cell_width) % 2
        if self.pacman.rect.left > self.x_cells * cell_width:
            self.pacman.rect.right = 0
        elif self.pacman.rect.right < 0:
            self.pacman.rect.left = self.x_cells * cell_width