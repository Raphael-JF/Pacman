"""Ce module contient toutes les constantes nécessaires au fonctionnement du programme."""

INIT_WINSIZE = [1280,720]
DEFAULT_WINSIZE = [800,450] #échelle pour laquelle on définit les valeurs de nos widgets
TIME_TICKING = 60 #temps in game (immutable)
START_GAME_FPS = 60 #fps au démarrage du jeu

GAME_RESOLUTIONS = [
    [800,450],
    [960,540],
    [1280,720],
    [1600,900],
    [1920,1080],
]


#Game_map_editor() :
GME_DEFAULT_POS = [400,270]
GME_TILE_SIZES = [10, 17, 24, 32, 39, 46, 53, 61, 68, 75]
GME_DEFAULT_DIMENSIONS = [10,10]
GME_TILE_SIZES = [16.0, 19.2, 22.4, 25.6, 28.8, 32.0, 35.2, 38.4, 41.6, 44.8, 48.0]
GME_VALUE_TO_NAMES = {
    "X" : ["textures","wall.png"],
    "■" : ["textures","wall.png"],
    "□" : ["textures","empty_tile.png"],
    "P" : ["textures","pacman","pacman_40.png"],
    "←" : ["textures","left_portal.png"],
    "→" : ["textures","right_portal.png"],
    "." : ["textures","coin.png"],
    "●" : ["textures","super_coin.png"]
}


# functions
def add_index(list,value,index):

    for i,val in enumerate(list):
        if val == value:
            if 0 <= i+index <= len(list)-1:
                return list[i+index]
            elif i+index > len(list)-1:
                return list[-1]
            elif 0 > i+index:
                return list[0]
    raise ValueError("not found")
