"""Ce module contient toutes les constantes et fonctions nécessaires au fonctionnement du programme."""

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
    "O" : ["textures","empty_tile.png"],
    "□" : ["textures","empty_tile.png"],
    "P" : ["textures","pacman","pacman_40.png"],
    "←" : ["textures","left_portal.png"],
    "→" : ["textures","right_portal.png"],
    "." : ["textures","coin.png"],
    "●" : ["textures","super_coin.png"]
}


# functions
from datetime import datetime
import os,tkinter
from tkinter import filedialog

def add_index(list,value,index):
    """
    cherche dans `list` `valeur` et ajoute `index` à l'index `valeur` se trouve dans `list`
    raise ValueError si `value not in list` est vraie
    """
    for i,val in enumerate(list):
        if val == value:
            if 0 <= i+index <= len(list)-1:
                return list[i+index]
            elif i+index > len(list)-1:
                return list[-1]
            elif 0 > i+index:
                return list[0]
    raise ValueError("not found")


def get_date():
    now = datetime.now()
    return now.strftime("%Y_%m_%d_%H-%M-%S")


def get_save_files():
    json_files = []
    for root, _, files in os.walk(os.path.join(os.getcwd(),'backup_files','map_editor')):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

def open_file_dialog():
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])
    root.destroy()
    return file_path

def open_save_dialog():
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(confirmoverwrite = True, defaultextension=".json", filetypes=[("Fichiers JSON", "*.json")])
    root.destroy()
    return file_path

