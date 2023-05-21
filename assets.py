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
GME_DEFAULT_DIMENSIONS = [15,15]
GME_TILE_SIZES = [16.0, 19.2, 22.4, 25.6, 28.8, 32.0, 35.2, 38.4, 41.6, 44.8, 48.0]
GME_VALUE_TO_NAMES = {
    "X" : ["textures","wall.png"],
    "■" : ["textures","wall.png"],
    "O" : ["textures","empty_tile.png"],
    "□" : ["textures","empty_tile.png"],
    "_" : ["textures","ghost_door.png"],
    "P" : ["textures","pacman","pacman_40.png"],
    "←" : ["textures","left_portal.png"],
    "→" : ["textures","right_portal.png"],
    "." : ["textures","coin.png"],
    "●" : ["textures","super_coin.png"]
}

#Game_map() :
PACMAN_SPEED = lambda cell_width : 4*cell_width
PACMAN_MOVING_SPRITES = [["textures","pacman","pacman_0.png"],["textures","pacman","pacman_20.png"],["textures","pacman","pacman_40.png"],["textures","pacman","pacman_60.png"],["textures","pacman","pacman_80.png"],["textures","pacman","pacman_60.png"],["textures","pacman","pacman_40.png"],["textures","pacman","pacman_20.png"]]
PACMAN_DYING_SPRITES = [["textures","pacman","pacman_0.png"],["textures","pacman","pacman_20.png"],["textures","pacman","pacman_40.png"],["textures","pacman","pacman_60.png"],["textures","pacman","pacman_80.png"],["textures","pacman","pacman_100.png"],["textures","pacman","pacman_120.png"],["textures","pacman","pacman_140.png"],["textures","pacman","pacman_160.png"],["textures","pacman","pacman_180.png"],["textures","pacman","pacman_200.png"],["textures","pacman","pacman_220.png"],["textures","pacman","pacman_240.png"],["textures","pacman","pacman_260.png"],["textures","pacman","pacman_280.png"],["textures","pacman","pacman_300.png"],["textures","pacman","pacman_320.png"],["textures","pacman","pacman_340.png"],["textures","pacman","pacman_360.png"]]
PACMAN_SPRITES_DELAY = 0.035
GHOST_SPRITES_DELAY = 0.1
GHOST_COLORS = ["red","blue","pink","orange","green","purple","brown","gray"]
GHOST_CHASING_TIME = lambda cell_x,cell_y,speed: cell_x*cell_y/speed**2.5
GHOST_CHASE_COOLDOWN = lambda nb_ghosts: 2*nb_ghosts
GHOST_ESCAPE_TIME = lambda cell_x,cell_y : ((cell_x*cell_y)**0.5)/3.5
GHOST_BLINK_DELAY = 0.35
GHOST_ESC_BLINK_TIME = 3 # temps de clignotement des fantômes en mode "escape"

# functions
import os,tkinter,math
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


def get_save_files():
    json_files = []
    for root, _, files in os.walk(os.path.join(os.getcwd(),'backup_files','map_editor')):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files


def get_progress():
    res = None
    for root, dirs, files in os.walk(os.path.join(os.getcwd(),'backup_files')):
        if "map_editor" in dirs:
            dirs.remove("map_editor")
        for file in files:
            if file == "progress.json":
                res = os.path.join(root, file)
    return res

def reset_progress(save_manager):
    save_manager.data = {
        "lvl1" : True,
        "lvl2" : False,
        "lvl3" : False,
        "lvl4" : False,
        "lvl5" : False,
        "lvl6" : False,
        "lvl7" : False,
        "lvl8" : False,
        "lvl9" : False,
        "lvl10" : False
    }
    save_manager.save(["progress.json"])

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

def search_type_in_list(lst:list,type:type):
    res = []
    for elt in lst:
        if isinstance(elt,type):
            res.append(elt)
    return res

def collide(sprite_a,sprite_b):
    return sprite_a.rect.colliderect(sprite_b)


def opposite_side(side):

    if side == "left":
        return "right"
    elif side == "right":
        return "left"
    elif side == "top":
        return "bottom"
    elif side == "bottom":
        return "top"
    
def closest_rect(rect, rect_list):

    closest_rect = rect_list.pop(0)
    closest_distance = math.sqrt((rect.centerx - closest_rect.centerx) ** 2 + (rect.centery - closest_rect.centery) ** 2)

    for r in rect_list:
        distance = math.sqrt((rect.centerx - r.centerx) ** 2 + (rect.centery - r.centery) ** 2)
        if distance < closest_distance:
            closest_distance = distance
            closest_rect = r
    return closest_rect


def farest_rect(rect,rect_list):

    farest_rect = rect_list.pop(0)
    max_distance = math.sqrt((rect.centerx - farest_rect.centerx) ** 2 + (rect.centery - farest_rect.centery) ** 2)

    for r in rect_list:
        distance = math.sqrt((rect.centerx - r.centerx) ** 2 + (rect.centery - r.centery) ** 2)
        if distance > max_distance:
            max_distance = distance
            farest_rect = rect
    return farest_rect