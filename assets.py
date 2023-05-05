"""Ce module contient toutes les constantes nécessaires au fonctionnement du programme."""

DEFAULT_SIZE = [800,450] #échelle pour laquelle on définit les valeurs de nos widgets
TIME_TICKING = 500 #temps in game (immutable)
START_GAME_FPS = 60 #fps au démarrage du jeu

GAME_RESOLUTIONS = [
            [1280,720],
            [800,450],
            [960,540],
            
            [1600,900],
            [1920,1080],
        ]


#Game_map_editor() :
TILE_SIZES = [10, 17, 24, 32, 39, 46, 53, 61, 68, 75]
GME_DEFAULT_DIMENSIONS = [9,8]


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
