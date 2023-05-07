import math,os
import assets,pygame
from classes.box import Box
from classes.image import Image
from classes.transition import transition_nbounds

import pygame,os

class Tile():
    """
    version ultra légère de Image
    """
    def __init__(
            self,
            width:int,
            name:list[str],
            value:str
    ):  
        self.value = value
        self.width = width
        self.contenu = pygame.image.load(os.path.join(os.getcwd(),'images',*name))
        self.calc_image()
    

    def calc_image(self):

        self.image = pygame.transform.smoothscale(self.contenu,(round(self.width),round(self.width)))


    def set_value(self,value:str):
        
        self.value = value
    

    def set_namevalue(self,name,value):

        self.contenu = pygame.image.load(os.path.join(os.getcwd(),'images',*name))
        self.value = value
        self.calc_image()


    def set_width(self,width):

        self.width = width
        self.calc_image()


class Game_map_editor(pygame.sprite.Sprite):

    def __init__(
            self,
            winsize:list,
            dimensions:list[int],
            loc:list,
            background_clr:list[int],
            parent_groups:list,
            living:bool,
            layer:int,


    ):    
        super().__init__()

        self.winsize = winsize
        self._layer = layer
        self.parent_groups = parent_groups
        self.pos = list(loc[0])
        self.placement_mode = loc[1]
        self.background_clr = background_clr
        self.border_clr = [134, 135, 210]

        self.x_tiles, self.y_tiles = dimensions
        if self.x_tiles % 2 == 0:
            self.x_tiles += 1
        if self.y_tiles % 2 == 1:
            self.y_tiles += 1

        self.tile_width = assets.GME_TILE_SIZES[len(assets.GME_TILE_SIZES)//2]
        self.tile_width_choices = assets.GME_TILE_SIZES

        self.border_width = self.tile_width/20
        self.border_width_choices = []
        for i in range(10):
            self.border_width_choices.append(transition_nbounds([self.tile_width/80,self.border_width,self.tile_width*7/80],[5,5],['linear','linear'],i))

        self.tiles:list[list[Tile]] = []
        for y in range(self.y_tiles):
            temp_tiles:list[Tile] = []
            for x in range(self.x_tiles):
                temp_tiles.append(Tile(
                    name = ["textures","empty_tile.png"],
                    width = self.tile_width,
                    value = "□"
                ))
            self.tiles.append(temp_tiles)

        for x in range(self.x_tiles):
            self.tiles[0][x].set_namevalue(["textures","wall.png"],"X")
            self.tiles[-1][x].set_namevalue(["textures","wall.png"],"X")
        
        for y in range(self.y_tiles):
            self.tiles[y][0].set_namevalue(["textures","wall.png"],"X")
            self.tiles[y][-1].set_namevalue(["textures","wall.png"],"X")

        x,y = self.x_tiles//2 - 2, self.y_tiles//2 - 2

        self.tiles[y][x].set_namevalue(["textures","wall.png"],"X")
        self.tiles[y][x+1].set_namevalue(["textures","wall.png"],"X")
        self.tiles[y][x+2].set_namevalue(["textures","empty_tile.png"],"O")
        self.tiles[y][x+3].set_namevalue(["textures","wall.png"],"X")
        self.tiles[y][x+4].set_namevalue(["textures","wall.png"],"X")

        self.tiles[y+1][x].set_namevalue(["textures","wall.png"],"X")
        self.tiles[y+1][x+1].set_namevalue(["textures","empty_tile.png"],"O")
        self.tiles[y+1][x+2].set_namevalue(["textures","empty_tile.png"],"O")
        self.tiles[y+1][x+3].set_namevalue(["textures","empty_tile.png"],"O")
        self.tiles[y+1][x+4].set_namevalue(["textures","wall.png"],"X")

        self.tiles[y+2][x].set_namevalue(["textures","wall.png"],"X")
        self.tiles[y+2][x+1].set_namevalue(["textures","empty_tile.png"],"O")
        self.tiles[y+2][x+2].set_namevalue(["textures","empty_tile.png"],"O")
        self.tiles[y+2][x+3].set_namevalue(["textures","empty_tile.png"],"O")
        self.tiles[y+2][x+4].set_namevalue(["textures","wall.png"],"X")

        self.tiles[y+3][x].set_namevalue(["textures","wall.png"],"X")
        self.tiles[y+3][x+1].set_namevalue(["textures","wall.png"],"X")
        self.tiles[y+3][x+2].set_namevalue(["textures","wall.png"],"X")
        self.tiles[y+3][x+3].set_namevalue(["textures","wall.png"],"X")
        self.tiles[y+3][x+4].set_namevalue(["textures","wall.png"],"X")

        self.tiles[y+4][x+2].set_namevalue(['textures','pacman','pacman_40.png'],'P')

        self.calc_image()
        self.calc_rect()

        if living:
            self.liven()


    def liven(self):
        """
        A l'inverse de kill() (méthode de pygame.sprite.Sprite permettant de suppprimer le sprite de tous les groupes dans lesquels il se trouve), ajoute le sprite à tous ses groupes parents.
        """

        for group in self.parent_groups:
            group.add(self)
            
        
    def calc_image(self):

        border_width = round(self.border_width / 2) * 2
        tile_width = round(self.tile_width)
        if border_width == 0:
            border_width = 2
        self.image = pygame.Surface([tile_width*self.x_tiles + border_width,tile_width*self.y_tiles + border_width],pygame.SRCALPHA)
        for y in range(self.y_tiles):
            for x in range(self.x_tiles):
                if self.tiles[y][x].width != tile_width:
                    self.tiles[y][x].set_width(tile_width)
                self.image.blit(self.tiles[y][x].image,[border_width//2+x*tile_width,border_width//2+y*tile_width])

        for x in range(self.x_tiles+1):
            pygame.draw.line(self.image,self.border_clr,[border_width//2-1+x*tile_width,0],[border_width//2-1+x*tile_width,self.image.get_height()-1],border_width)
        for y in range(self.y_tiles+1):
            pygame.draw.line(self.image,self.border_clr,[0,border_width//2-1+y*tile_width],[self.image.get_width()-1,border_width//2-1+y*tile_width],border_width)


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


    def update(self,new_winsize,dt,cursor) -> None:
        """Actualisation du sprite ayant lieu à chaque changement image"""

        if self.winsize != new_winsize:
            self.rescale(new_winsize)


    def rescale(self,new_winsize):
        
        old_winsize = self.winsize[:]
        self.winsize = new_winsize
        self.ratio = self.winsize[0] / old_winsize[0]

        self.tile_width_choices = [i*self.ratio for i in self.tile_width_choices]
        self.border_width_choices = [i*self.ratio for i in self.border_width_choices]
        self.border_width *= self.ratio
        self.pos = [i*self.ratio for i in self.pos]
        self.tile_width *= self.ratio
        for y in range(self.y_tiles):
            for x in range(self.x_tiles):
                self.tiles[y][x].set_width(self.tile_width)
        self.calc_image()
        self.calc_rect()


    def offset(self,pos):

        self.pos[0] += pos[0]
        self.pos[1] += pos[1]
        self.calc_rect()

    
    def change_size_index(self,index):

        self.tile_width = assets.add_index(self.tile_width_choices,self.tile_width,index)
        self.border_width = assets.add_index(self.border_width_choices,self.border_width,index)
        self.calc_image()
        self.calc_rect()


    def get_tile(self,abs_pos):

        tile_width = round(self.tile_width)
        rel_pos = [abs_pos[i] - self.rect.topleft[i] for i in range(2)]
        y,x = rel_pos[1]//tile_width,rel_pos[0]//tile_width
        if y >= self.y_tiles:
            y = self.y_tiles-1
        if x >= self.x_tiles:
            x = self.x_tiles-1

        return self.tiles[int(y)][int(x)]
    
    
    def get_abs_center(self,tile):
        
        y,x = self.search_tile(tile)
        pos = round(self.border_width/2)+(x+0.5)*round(self.tile_width),round(self.border_width/2)+(y+0.5)*round(self.tile_width)
        return [pos[i] + self.rect.topleft[i] for i in range(2)]
    
    
    def symetric_tile(self,tile,axis=""):
        
        y,x = self.search_tile(tile)
        if axis == "x":
            x = self.x_tiles - x - 1
        elif axis == "y":
            y = self.y_tiles - y - 1
        else:
            x = self.x_tiles - x - 1
            y = self.y_tiles - y - 1
        
        return self.tiles[y][x]

    
    def search_tile(self,tile):
        """
        Recherche naïve d'une tuile dans la matrice de l'objet.
        """
        for y in range(self.y_tiles):
            for x in range(self.x_tiles):
                if tile is self.tiles[y][x]:
                    return [y,x]
                
    
    def get_matrix(self):
        
        matrix = ""
        for y in range(self.y_tiles):
            for x in range(self.x_tiles):
                matrix += self.tiles[y][x].value
            matrix += "\n"
        return matrix



    def set_tile_value(self,tile:Tile,value):
    
        tile.set_namevalue(assets.GME_VALUE_TO_NAMES[value],value)
        y,x = self.search_tile(tile)

        border_width = round(self.border_width / 2) * 2
        tile_width = round(self.tile_width)
        if border_width == 0:
            border_width = 2
        
        if value in ["←","→","□"]:
            pygame.draw.rect(self.image,[0,0,0,0],pygame.Rect([x*self.tile_width+border_width//2,y*self.tile_width+border_width//2],[self.tile_width]*2))

        self.image.blit(tile.image,[border_width//2+x*tile_width,border_width//2+y*tile_width])
        for i in range(2):
            pygame.draw.line(self.image,self.border_clr,[border_width//2-1+(x+i)*tile_width,0],[border_width//2-1+(x+i)*tile_width,self.image.get_height()-1],border_width)
            pygame.draw.line(self.image,self.border_clr,[0,border_width//2-1+(y+i)*tile_width],[self.image.get_width()-1,border_width//2-1+(y+i)*tile_width],border_width)
        
        if value == "P":
            for i in range(self.y_tiles):
                for j in range(self.x_tiles):
                    if self.tiles[i][j] is not tile and self.tiles[i][j].value == "P" :
                        pygame.draw.rect(self.image,[0,0,0,0],pygame.Rect([j*self.tile_width+border_width//2,i*self.tile_width+border_width//2],[self.tile_width]*2))
                        self.set_tile_value(self.tiles[i][j],"□")
                        return 

