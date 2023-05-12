import pygame,os,assets
from classes.json_handler import JSON_handler
from classes.image import Image

class Wall(Image):

    def __init__(self,winsize,center,width):

        super().__init__(
            name = ["textures","wall.png"],
            winsize = winsize,
            scale_axis = [width,"x"],
            loc = [center,"center"],
            parent_groups = [],
            border = [-1,[0,0,0,0],0,"inset"],
        )






class Game_map():

    def __init__(
        self,
        winsize,
        lvl_path,
        parent_groups,
        layer = 0,
        living = True,
    ):

        self.winsize = winsize
        self._layer = layer
        self.lvl_path = lvl_path
        self.parent_groups = parent_groups
        self.save_manager = JSON_handler()
        self.save_manager.read(lvl_path)
        matrix = self.save_manager["matrix"]

        self.x_tiles = len(matrix[0:matrix.find("\n")])
        self.y_tiles = matrix.count("\n")
        self.cell_width = min(self.winsize[0] // self.x_tiles, self.winsize[1] // self.y_tiles)

        if living:
            self.liven()
    
    def liven(self):
        """
        A l'inverse de kill() (méthode de pygame.sprite.Sprite permettant de suppprimer le sprite de tous les groupes dans lesquels il se trouve), ajoute le sprite à tous ses groupes parents.
        """

        for group in self.parent_groups:
            group.add(self)


    def calc_image(self):

        pass
