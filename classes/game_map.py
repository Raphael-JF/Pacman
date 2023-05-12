import pygame,os,assets
from classes.json_handler import JSON_handler

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

    def __repr__(self):
        return self.value


class Game_map():

    def __init__(self,lvl_path,winsize):
        self.lvl_path = lvl_path
        self.save_manager = JSON_handler()
        self.save_manager.read(lvl_path)
        

        self.x_tiles = len(matrix[0:matrix.find("\n")])
        self.y_tiles = matrix.count("\n")
        i = 0
        matrix = matrix.replace("\n","")
        self.tiles:list[list[Tile]] = []
        for y in range(self.y_tiles):
            temp_tiles:list[Tile] = []
            for x in range(self.x_tiles):
                temp_tiles.append(Tile(
                    name = assets.GME_VALUE_TO_NAMES[matrix[i]],
                    width = self.tile_width,
                    value = matrix[i]
                ))
                i+=1
            self.tiles.append(temp_tiles)
        self.calc_image()
        self.calc_rect()