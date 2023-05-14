import pygame,os,assets
from classes.json_handler import JSON_handler
from classes.blocks import *


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

        for y in range(self.y_cells):
            for x in range(self.x_cells):
                self.set_neighbors(y,x)

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

        if self.pacman.direction is None:
            return
        

        self.pacman.rect = self.pacman.get_next_rect(dt)
        colliding = pygame.sprite.spritecollide(self.pacman,self.group,False,lambda a,b :a.rect.colliderect(b.rect))
        walls = [sprite for sprite in colliding if isinstance(sprite, Wall) or isinstance(sprite,Ghost_door)]
        if walls:
            wall = walls[0]
            if self.pacman.direction == "top" and self.pacman.rect.top <= wall.rect.bottom:
                self.pacman.rect.top = wall.rect.bottom #-1
            elif self.pacman.direction == "bottom" and self.pacman.rect.bottom >= wall.rect.top:
                self.pacman.rect.bottom = wall.rect.top #+1
            elif self.pacman.direction == "left" and self.pacman.rect.left <= wall.rect.right:
                self.pacman.rect.left = wall.rect.right #-1
            elif self.pacman.direction == "right" and self.pacman.rect.right >= wall.rect.left:
                self.pacman.rect.right = wall.rect.left #+1

        # under_pacman = self.locate_cell(self.pacman.rect.center)
        # pygame.draw.rect(self.image,[0,0,0,0],under_pacman.rect)
        # self.image.blit(under_pacman.image,under_pacman.rect)
        # if under_pacman.next["top"] is not None:
        #     pygame.draw.rect(self.image,[0,0,0,0],under_pacman.next["top"].rect)
        #     self.image.blit(under_pacman.next["top"].image,under_pacman.next["top"].rect)
        # if under_pacman.next["bottom"] is not None:
        #     pygame.draw.rect(self.image,[0,0,0,0],under_pacman.next["bottom"].rect)
        #     self.image.blit(under_pacman.next["bottom"].image,under_pacman.next["bottom"].rect)
        # if under_pacman.next["left"] is not None:
        #     pygame.draw.rect(self.image,[0,0,0,0],under_pacman.next["left"].rect)
        #     self.image.blit(under_pacman.next["left"].image,under_pacman.next["left"].rect)
        # if under_pacman.next["right"] is not None:
        #     pygame.draw.rect(self.image,[0,0,0,0],under_pacman.next["right"].rect)
        #     self.image.blit(under_pacman.next["right"].image,under_pacman.next["right"].rect)
        # self.image.blit(self.pacman.image,self.pacman.rect)
        self.calc_image()



    def rescale(self,new_winsize):
        
        old_winsize = self.winsize[:]
        self.winsize = new_winsize
        self.ratio = self.winsize[0] / old_winsize[0]
        self.pos = [i*self.ratio for i in self.pos]
        self.cell_width *= self.ratio
        for y in range(self.y_cells):
            for x in range(self.x_cells):
                self.cells[y][x].rescale(new_winsize)
        self.pacman.rescale(new_winsize)
        self.calc_image()
        self.calc_rect()


    def set_neighbors(self,y,x):

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
    
    def handle_input(self, keys):

        if keys[pygame.K_LEFT]:
            self.pacman.direction = "left"
        elif keys[pygame.K_RIGHT]:
            self.pacman.direction = "right"
        elif keys[pygame.K_UP]:
            self.pacman.direction = "top"
        elif keys[pygame.K_DOWN]:
            self.pacman.direction = "bottom"


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