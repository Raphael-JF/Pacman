import pygame,assets,sys
from classes.image import Image
from classes.box import Box
from classes.timer import Timer
from classes.title import Title
from classes.button import Button
from classes.json_handler import JSON_handler
from classes.game_map import Game_map

all_group = pygame.sprite.Group()
to_draw_group = pygame.sprite.LayeredUpdates()
clickable_group = pygame.sprite.LayeredUpdates()
fps_display_update = Timer(0)

background = Box(
    winsize = assets.DEFAULT_WINSIZE,
    size = [800,450],
    loc = [[0,0],"topleft"],
    background_clr=(17, 19, 166),
    border = [-1,(0,0,0),0,"inset"],
    parent_groups = [all_group, to_draw_group],
)

dark_background = Box(
    winsize = assets.DEFAULT_WINSIZE,
    size = [800,450],
    loc = [[0,0],"topleft"],
    background_clr = [0,0,0],
    border = [-1,(0,0,0),0,"inset"],
    alpha = 0,
    parent_groups = [all_group, to_draw_group],
    living = False,
    layer = 10
)

start_title = Title(
    winsize = assets.DEFAULT_WINSIZE, 
    loc = [[400,225],"center"], 
    background_clr = [0,0,0,0],
    size = [400 ,60],
    border=[-1,(0,0,0,0),0,"inset"],
    text = "Commandez pour jouer",
    font_clrs = [[240,240,240]],
    font_size = 50,
    font_family = "RopaSans-Regular.ttf",
    parent_groups = [all_group,to_draw_group],
    living = False,
    layer = 11
)

fps_display = Title(
    winsize = assets.DEFAULT_WINSIZE, 
    loc = [(0,0),"topleft"], 
    background_clr = (0,0,0,0),
    size = [100 ,40],
    border=[-1,(0,0,0,0),0,"inset"],
    text = "",
    font_clrs = [(0, 117, 12),(0, 117, 12)],
    font_size = 20,
    font_family = "RopaSans-Regular.ttf",
    layer = 100_000,
    parent_groups = [all_group,to_draw_group],
    living = False
)

coin_image = Image(
    name = ["textures","coin_logo.png"],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [18,'x'],
    loc = [[20,20],"center"],
    border = [-1,[0,0,0],0,"inset"],
    layer = 1,
    parent_groups = [all_group, to_draw_group],
)

coin_count = Title(
    winsize = assets.DEFAULT_WINSIZE, 
    loc = [[35,20],"midleft"], 
    background_clr = (0,0,0,0),
    size = [58,40],
    border=[-1,(0,0,0,0),0,"inset"],
    text = "888/888",
    font_clrs = [[240,240,240]],
    font_size = 21,
    font_family = "LiberationMono-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group],
    living = True
)

super_coin_image = Image(
    name = ["textures","super_coin_logo.png"],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [25,'x'],
    loc = [[20,50],"center"],
    border = [-1,[0,0,0],0,"inset"],
    layer = 1,
    parent_groups = [all_group, to_draw_group],
)

super_coin_count = Title(
    winsize = assets.DEFAULT_WINSIZE, 
    loc = [[35,50],"midleft"], 
    background_clr = (0,0,0,0),
    size = [58,40],
    border=[-1,(0,0,0,0),0,"inset"],
    text = "888/888",
    font_clrs = [[240,240,240]],
    font_size = 21,
    font_family = "LiberationMono-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group],
    living = True
)


game_map = None

cells:list[Image] = []


def loop(screen,new_winsize, dt, new_lvl_path, fps_infos):
    global game_map

    if fps_display.alive() != fps_infos[1]:
        if fps_infos[1]:
            fps_display.liven()
        else:
            fps_display.kill()
    fps_display_update.pass_time(dt)
    if fps_infos[1] and fps_display_update.finished:
        fps_display.set_text(f"max fps : {fps_infos[0]}\nfps : {1/dt:.2f}")
        fps_display_update.__init__(1)

    if game_map is None:
        game_map = Game_map(
            winsize = new_winsize,
            loc = [[400,225],"center"],
            lvl_path = new_lvl_path,
            size = [600,450],
            parent_groups = [all_group,to_draw_group],
            layer = 1)
        show_start_title()
        

    cursor = pygame.mouse.get_pos()

    hovered_clickable:Button = (clickable_group.get_sprites_at(cursor) or [None])[-1]
    if hovered_clickable is not None:
        hovered_clickable.set_hovering(True)
    for btn in clickable_group.sprites():
        if btn is not hovered_clickable:
            btn.set_hovering(False)
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in (pygame.BUTTON_LEFT,pygame.BUTTON_RIGHT):
                if hovered_clickable != None :
                    hovered_clickable.set_clicking(True)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button in (pygame.BUTTON_LEFT,pygame.BUTTON_RIGHT): 
                res = None
                if hovered_clickable != None :
                    if hovered_clickable.clicking:
                        res = button_handling(hovered_clickable)
                for btn in clickable_group.sprites():
                    btn.set_clicking(False)
                return res
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return 0
            elif event.key in [pygame.K_UP,pygame.K_z]:
                if start_title.alpha == 255:
                    hide_start_title()
                game_map.handle_input("top")
            elif event.key in [pygame.K_DOWN,pygame.K_s]:
                if start_title.alpha == 255:
                    hide_start_title()
                game_map.handle_input("bottom")
            elif event.key in [pygame.K_LEFT,pygame.K_q]:
                if start_title.alpha == 255:
                    hide_start_title()
                game_map.handle_input("left")
            elif event.key in [pygame.K_RIGHT,pygame.K_d]:
                if start_title.alpha == 255:
                    hide_start_title()
                game_map.handle_input("right")
    
    update_counts()
    for btn in clickable_group.sprites():
        manage_states(btn)
    all_group.update(new_winsize,dt,cursor)
    to_draw_group.draw(screen)
    pygame.display.flip()

def manage_states(btn):
    pass

def button_handling(clickable:Button):
    pass


def show_start_title():
    dark_background.instant_change_alpha([0,85],[0.2],["out"])
    start_title.instant_change_alpha([0,255],[0.2],["out"])
    start_title.instant_translate([[400,175],[400,225]],[0.2],["out"])

def hide_start_title():
    dark_background.instant_change_alpha([85,0],[0.2],["in"])
    start_title.instant_change_alpha([255,0],[0.2],["in"])
    start_title.instant_translate([[400,225],[400,175]],[0.2],["in"])
    game_map.set_pause(False)

def update_counts():
    coin_count.set_text(f"{game_map.max_nb_coins-game_map.nb_coins}/{game_map.max_nb_coins}")
    super_coin_count.set_text(f"{game_map.max_nb_super_coins-game_map.nb_super_coins}/{game_map.max_nb_super_coins}")