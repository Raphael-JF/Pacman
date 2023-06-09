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
    background_clr=[0,0,0],
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

pause_background = Box(
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

pause_title = Title(
    winsize = assets.DEFAULT_WINSIZE, 
    loc = [[400,175],"center"], 
    background_clr = [0,0,0,0],
    size = [400 ,80],
    border=[-1,(0,0,0,0),0,"inset"],
    text = "Pause",
    font_clrs = [[240,240,240]],
    font_size = 70,
    font_family = "RopaSans-Regular.ttf",
    parent_groups = [all_group,to_draw_group],
    living = False,
    layer = 11
)

lose_title = Title(
    winsize = assets.DEFAULT_WINSIZE, 
    loc = [[400,175],"center"], 
    background_clr = [0,0,0,0],
    size = [400 ,80],
    border=[-1,(0,0,0,0),0,"inset"],
    text = "Vous avez perdu",
    font_clrs = [[240,240,240]],
    font_size = 70,
    font_family = "RopaSans-Regular.ttf",
    parent_groups = [all_group,to_draw_group],
    living = False,
    layer = 11
)

win_title = Title(
    winsize = assets.DEFAULT_WINSIZE, 
    loc = [[400,175],"center"], 
    background_clr = [0,0,0,0],
    size = [400 ,80],
    border=[-1,(0,0,0,0),0,"inset"],
    text = "Vous avez gagné",
    font_clrs = [[240,240,240]],
    font_size = 70,
    font_family = "RopaSans-Regular.ttf",
    parent_groups = [all_group,to_draw_group],
    living = False,
    layer = 11
)

leave = Button(
    winsize = assets.DEFAULT_WINSIZE, 
    loc = [[300,300],"center"], 
    background_clr = [250,250,250],
    size = [160,40],
    border=[2,[25,25,25],2,"inset"],
    text = "Quitter",
    font_clrs=[[25,25,25]],
    font_size=32,
    font_family="RopaSans-Regular.ttf",
    layer = 11,
    parent_groups = [all_group, to_draw_group, clickable_group],
    living = False
)

play_again = Button(
    winsize = assets.DEFAULT_WINSIZE, 
    loc = [[500,300],"center"], 
    background_clr = [250,250,250],
    size = [160,40],
    border=[2,[25,25,25],2,"inset"],
    text = "Rejouer",
    font_clrs=[[25,25,25]],
    font_size=32,
    font_family="RopaSans-Regular.ttf",
    layer = 11,
    parent_groups = [all_group, to_draw_group, clickable_group],
    living = False
)


game_map = None
basic_buttons = [leave,play_again]


def loop(screen,new_winsize, dt, lvl_path, fps_infos):
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
            lvl_path = lvl_path,
            size = [600,450],
            parent_groups = [all_group,to_draw_group],
            layer = 1)
        show_start_screen()
        

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
                if not dark_background.alive():
                    if pause_background.alive():
                        game_map.pause = False
                        hide_pause_screen()
                    else:
                        game_map.pause = True
                        show_pause_screen()
            elif event.key in [pygame.K_UP,pygame.K_z]:
                if start_title.alive():
                    if start_title.alpha == 255:
                        hide_start_scren()
                        game_map.handle_input("top")
                else:
                    game_map.handle_input("top")
            elif event.key in [pygame.K_DOWN,pygame.K_s]:
                if start_title.alive():
                    if start_title.alpha == 255:
                        hide_start_scren()
                        game_map.handle_input("bottom")
                else:
                    game_map.handle_input("bottom")
            elif event.key in [pygame.K_LEFT,pygame.K_q]:
                if start_title.alive():
                    if start_title.alpha == 255:
                        hide_start_scren()
                        game_map.handle_input("left")
                else:
                    game_map.handle_input("left")
            elif event.key in [pygame.K_RIGHT,pygame.K_d]:
                if start_title.alive():
                    if start_title.alpha == 255:
                        hide_start_scren()
                        game_map.handle_input("right")
                else:
                    game_map.handle_input("right")
            
            elif event.key == pygame.K_l:
                game_map.finished = True
                game_map.nb_coins = 0
                game_map.nb_super_coins = 0

    coin_count.set_text(f"{game_map.max_nb_coins-game_map.nb_coins}/{game_map.max_nb_coins}")
    super_coin_count.set_text(f"{game_map.max_nb_super_coins-game_map.nb_super_coins}/{game_map.max_nb_super_coins}")
    if game_map.finished and not dark_background.alive():
        if not game_map.pacman.alive():
            show_lose_screen()
        else:
            show_win_screen()
            return 10

    for btn in clickable_group.sprites():
        manage_states(btn)
    all_group.update(new_winsize,dt,cursor)
    to_draw_group.draw(screen)
    pygame.display.flip()


def show_start_screen():
    dark_background.instant_change_alpha([0,85],[0.35],["out"])
    start_title.instant_change_alpha([0,255],[0.35],["out"])
    start_title.instant_translate([[400,175],[400,225]],[0.35],["out"])
def hide_start_scren():
    dark_background.instant_change_alpha([85,0],[0.25],["in"])
    start_title.instant_change_alpha([255,0],[0.25],["in"])
    start_title.instant_translate([[400,225],[400,175]],[0.25],["in"])
    game_map.set_pause(False)

def show_pause_screen():
    pause_background.instant_change_alpha([0,135],[0.35],["out"])
    pause_title.instant_change_alpha([0,255],[0.35],["out"])
    pause_title.instant_translate([[400,125],[400,175]],[0.35],["out"])
    leave.instant_change_alpha([0,255],[0.35],["out"])
    play_again.instant_change_alpha([0,255],[0.35],["out"])
def hide_pause_screen():
    pause_background.instant_change_alpha([135,0],[0.15],["in"])
    pause_title.instant_change_alpha([255,0],[0.15],["in"])
    pause_title.instant_translate([[400,175],[400,125]],[0.15],["in"])
    leave.instant_change_alpha([255,0],[0.15],["in"])
    play_again.instant_change_alpha([255,0],[0.15],["in"])

def show_lose_screen():
    dark_background.instant_change_alpha([0,135],[0.35],["out"])
    lose_title.instant_change_alpha([0,255],[0.35],["out"])
    lose_title.instant_translate([[400,125],[400,175]],[0.35],["out"])
    leave.instant_change_alpha([0,0,255],[1,0.35],["linear","out"])
    play_again.instant_change_alpha([0,0,255],[1,0.35],["linear","out"])

def show_win_screen():
    dark_background.instant_change_alpha([0,135],[0.35],["out"])
    win_title.instant_change_alpha([0,255],[0.35],["out"])
    win_title.instant_translate([[400,125],[400,175]],[0.35],["out"])
    leave.instant_change_alpha([0,0,255],[1,0.35],["linear","out"])
    play_again.instant_change_alpha([0,0,255],[1,0.35],["linear","out"])


def manage_states(clickable:Button):

    if not clickable.clicking_changed and not clickable.hovering_changed:
        return
    
    if clickable in basic_buttons:
        if not clickable.hovering and not clickable.clicking:
            clickable.instant_change_background_clr([clickable.background_clr[:],[250,250,250]],[0.25],["inout"])
            clickable.instant_change_border_width([clickable.border_width,2],[0.25],["inout"])
            clickable.instant_change_border_padding([clickable.border_padding,2],[0.25],["inout"])
        elif clickable.hovering and not clickable.clicking:
            clickable.instant_change_background_clr([clickable.background_clr[:],[230,230,230]],[0.25],["inout"])
            clickable.instant_change_border_width([clickable.border_width,2],[0.25],["inout"])
            clickable.instant_change_border_padding([clickable.border_padding,0],[0.25],["inout"])
        elif clickable.hovering and clickable.clicking:
            if clickable.clicking_changed and not clickable.hovering_changed:
                clickable.instant_change_background_clr([clickable.background_clr[:],[210,210,210]],[0.25],["inout"])
                clickable.instant_change_border_width([clickable.border_width,3],[0.25],["inout"])
                clickable.instant_change_border_padding([clickable.border_padding,0],[0.25],["inout"])
        elif not clickable.hovering and clickable.clicking:
                clickable.instant_change_background_clr([clickable.background_clr[:],[210,210,210]],[0.25],["inout"])
                clickable.instant_change_border_width([clickable.border_width,3],[0.25],["inout"])
                clickable.instant_change_border_padding([clickable.border_padding,0],[0.25],["inout"])

def button_handling(clickable:Button):

    if clickable is leave:
        return 0
    
    elif clickable is play_again:
        return 1

