"""
Ce module contient les éléments et widgets du menu de campagne. Il contient aussi le code de gestion utilisateur pour ce menu.
"""

import pygame,sys,assets,os
pygame.init()
from classes.timer import Timer
from classes.box import Box
from classes.button import Button
from classes.title import Title
from classes.image_button import Image_button
from classes.game_map_editor import Game_map_editor
from classes.image import Image
from classes.json_handler import JSON_handler
from classes.slider import Slider

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
    layer = 0
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

center = Button(
    winsize = assets.DEFAULT_WINSIZE, 
    loc = [(16,441),"bottomleft"], 
    background_clr = [250,250,250],
    size = [60 ,20],
    border=[2,[25,25,25],1,"inset"],
    text = "Centrer",
    font_clrs=[[25,25,25]],
    font_size=16,
    font_family="RopaSans-Regular.ttf",
    layer = 4,
    parent_groups = [all_group, to_draw_group, clickable_group],
)

game_map = Game_map_editor(
    winsize = assets.DEFAULT_WINSIZE,
    dimensions = assets.GME_DEFAULT_DIMENSIONS,
    loc = [[400,270],"center"],
    background_clr = [0,0,0,0],
    parent_groups = [all_group,to_draw_group],
    living = True,
    layer = 2
)

block_overlay = Image(
    winsize = assets.DEFAULT_WINSIZE,
    name = ["textures","empty_tile.png"],
    scale_axis = [game_map.tile_width-game_map.border_width,'x'],
    loc = [[0,0],"center"],
    border = [-1,[0,0,0],0,'inset'],
    parent_groups = [all_group,to_draw_group],
    layer = 3,
    living = True
)
block_overlay_hor = Image(
    winsize = assets.DEFAULT_WINSIZE,
    name = ["textures","empty_tile.png"],
    scale_axis = [game_map.tile_width-game_map.border_width,'x'],
    loc = [[0,0],"center"],
    border = [-1,[0,0,0],0,'inset'],
    parent_groups = [all_group,to_draw_group],
    layer = 3,
    living = True
)

block_overlay_ver = Image(
    winsize = assets.DEFAULT_WINSIZE,
    name = ["textures","empty_tile.png"],
    scale_axis = [game_map.tile_width-game_map.border_width,'x'],
    loc = [[0,0],"center"],
    border = [-1,[0,0,0],0,'inset'],
    parent_groups = [all_group,to_draw_group],
    layer = 3,
    living = True
)

block_overlay_both = Image(
    winsize = assets.DEFAULT_WINSIZE,
    name = ["textures","empty_tile.png"],
    scale_axis = [game_map.tile_width-game_map.border_width,'x'],
    loc = [[0,0],"center"],
    border = [-1,[0,0,0],0,'inset'],
    parent_groups = [all_group,to_draw_group],
    layer = 3,
    living = True
)

buttons_container = Box(
    winsize = assets.DEFAULT_WINSIZE,
    size = [806,92],
    loc = [[-3,-3],"topleft"],
    background_clr = [0,0,0,200],
    parent_groups = [all_group,to_draw_group],
    border = [1.5,[175,175,175,200],0,'inset'],
    layer = 10 
)

wall = Image_button(
    name = ['textures','wall.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[42.75,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 11
)

coin = Image_button(
    name = ['textures','coin.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[123.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 11
)

super_coin = Image_button(
    name = ['textures','super_coin.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[203.75,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 11
)

pacman = Image_button(
    name = ['textures','pacman','pacman_40.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[284.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 11
)

portal = Image_button(
    name = ['textures','right_portal.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[364.75,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 11
)

trash_can = Image_button(
    name = ['textures','trash_can.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[445.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 11
)

placement_options = [wall,coin,super_coin,pacman,portal,trash_can]

separator = Box(
    winsize = assets.DEFAULT_WINSIZE,
    size = [2,62.5],
    loc = [[520.75,42.75],'center'],
    background_clr = [0,0,0,75],
    parent_groups = [all_group,to_draw_group],
    border = [3,[215,215,215],0,'inset'],
    layer = 11
)

horizontal_symetry = Image_button(
    name = ['textures','horizontal_symetry.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[596.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 11
)

vertical_symetry = Image_button(
    name = ['textures','vertical_symetry.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[676.75,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 11
)

hamburger = Image_button(
    name = ['textures','hamburger.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[757.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 11
)

hamburger_container = Box(
    winsize = assets.DEFAULT_WINSIZE,
    loc = [[1006.5,455],"bottomright"],
    size = [205,366],
    background_clr = [0,0,0,200],
    parent_groups = [all_group,to_draw_group],
    border = [1.5,[175,175,175,200],0,'inset'],
    layer = 5
)

hamburger_cross = Image_button(
    name = ['textures','white_cross.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [26,'x'],
    loc = [[820,108],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 6
)

hamburger_title = Title(
    winsize = assets.DEFAULT_WINSIZE,
    loc = [[901,108],'center'],
    background_clr = (235,235,235),
    size = [75 ,24],
    border=[2,(25,25,25),0,"inset"],
    text = "Menu",
    font_clrs = [(25,25,25)],
    font_size = 22,
    font_family = "RopaSans-Regular.ttf",
    layer = 6,
    parent_groups = [all_group,to_draw_group]
)

hamburger_open = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [[901,193],"center"],
    background_clr = (250,250,250),
    size = [135,32],
    border=[2,(25,25,25),2,"inset"],
    text = "Ouvrir",
    font_clrs=[(25,25,25)],
    font_size=25,
    font_family="RopaSans-Regular.ttf",
    layer = 6,
    parent_groups = [all_group,to_draw_group,clickable_group]  
)

hamburger_save = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [[901,230],"center"],
    background_clr = (250,250,250),
    size = [135,32],
    border=[2,(25,25,25),2,"inset"],
    text = "Enregistrer",
    font_clrs=[(25,25,25)],
    font_size=25,
    font_family="RopaSans-Regular.ttf",
    layer = 6,
    parent_groups = [all_group,to_draw_group,clickable_group]  
)

hamburger_play = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [[901,267],"center"],
    background_clr = (250,250,250),
    size = [135,32],
    border=[2,(25,25,25),2,"inset"],
    text = "Jouer",
    font_clrs=[(25,25,25)],
    font_size=25,
    font_family="RopaSans-Regular.ttf",
    layer = 6,
    parent_groups = [all_group,to_draw_group,clickable_group]  
)

hamburger_options = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [[901,341],"center"],
    background_clr = (250,250,250),
    size = [135,32],
    border=[2,(25,25,25),2,"inset"],
    text = "Options",
    font_clrs=[(25,25,25)],
    font_size=25,
    font_family="RopaSans-Regular.ttf",
    layer = 6,
    parent_groups = [all_group,to_draw_group,clickable_group]  
)

hamburger_leave = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [[901,378],"center"],
    background_clr = (250,250,250),
    size = [135,32],
    border=[2,(25,25,25),2,"inset"],
    text = "Quitter",
    font_clrs=[(25,25,25)],
    font_size=25,
    font_family="RopaSans-Regular.ttf",
    layer = 6,
    parent_groups = [all_group,to_draw_group,clickable_group]  
)

options_container = Box(
    winsize = assets.DEFAULT_WINSIZE,
    loc = [[1006.5,455],"bottomright"],
    size = [205,366],
    background_clr = [0,0,0,200],
    parent_groups = [all_group,to_draw_group],
    border = [1.5,[175,175,175,200],0,'inset'],
    layer = 3
)

options_cross = Image_button(
    name = ['textures','white_cross.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [26,'x'],
    loc = [[820,108],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 4
)

options_title = Title(
    winsize = assets.DEFAULT_WINSIZE,
    loc = [[901,108],'center'],
    background_clr = (235,235,235),
    size = [75 ,24],
    border=[2,(25,25,25),0,"inset"],
    text = "Options",
    font_clrs = [(25,25,25)],
    font_size = 22,
    font_family = "RopaSans-Regular.ttf",
    layer = 4,
    parent_groups = [all_group,to_draw_group]
)

options_width = Slider(
    winsize = assets.DEFAULT_WINSIZE,
    loc = [[901,193],"center"],
    background_clr= [250,250,250],
    font_clrs=[[25,25,25]],
    font_size=25,
    size = [135,32],
    options_list = [str(i) for i in range(9,31)],
    base_option = '15',
    anchor_options = True,
    cursor_width = 10,
    cursor_background_clr = [175,175,175],
    cursor_border = [2,(25,25,25)],
    border = [2,(25,25,25),0,"inset"],
    text = "Largeur : {}",
    font_family = "RopaSans-Regular.ttf",
    parent_groups= [all_group, to_draw_group, clickable_group],
    layer = 4,
)

options_height = Slider(
    winsize = assets.DEFAULT_WINSIZE,
    loc = [[901,230],"center"],
    background_clr= [250,250,250],
    font_clrs=[[25,25,25]],
    font_size=25,
    size = [135,32],
    options_list = [str(i) for i in range(8,31)],
    base_option = '15',
    anchor_options = True,
    cursor_width = 10,
    cursor_background_clr = [175,175,175],
    cursor_border = [2,(25,25,25)],
    border = [2,(25,25,25),0,"inset"],
    text = "Hauteur : {}",
    font_family = "RopaSans-Regular.ttf",
    parent_groups= [all_group, to_draw_group, clickable_group],
    layer = 4,
)

options_ghosts = Slider(
    winsize = assets.DEFAULT_WINSIZE,
    loc = [[901,267],"center"],
    background_clr= [250,250,250],
    font_clrs=[[25,25,25]],
    font_size=25,
    size = [135,32],
    options_list = [str(i) for i in range(2,9)],
    base_option = '4',
    anchor_options = True,
    cursor_width = 10,
    cursor_background_clr = [175,175,175],
    cursor_border = [2,(25,25,25)],
    border = [2,(25,25,25),0,"inset"],
    text = "Fantômes : {}",
    font_family = "RopaSans-Regular.ttf",
    parent_groups= [all_group, to_draw_group, clickable_group],
    layer = 4,
)

options_apply = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [[901,341],"center"],
    background_clr = (250,250,250),
    size = [135,32],
    border=[2,(25,25,25),2,"inset"],
    text = "Appliquer",
    font_clrs=[(25,25,25)],
    font_size=25,
    font_family="RopaSans-Regular.ttf",
    layer = 4,
    parent_groups = [all_group,to_draw_group,clickable_group]  
)

options_reset = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [[901,378],"center"],
    background_clr = (250,250,250),
    size = [135,32],
    border=[2,(25,25,25),2,"inset"],
    text = "Réinitialiser",
    font_clrs=[(25,25,25)],
    font_size=25,
    font_family="RopaSans-Regular.ttf",
    layer = 4,
    parent_groups = [all_group,to_draw_group,clickable_group]  
)


save_manager = JSON_handler({"matrix":game_map.get_matrix(),"nb_ghosts":4})


overlays = [block_overlay,block_overlay_hor,block_overlay_ver,block_overlay_both]
hotbar = [wall,coin,super_coin,pacman,portal,trash_can,horizontal_symetry,vertical_symetry,hamburger]
hotbar_blocks = [wall,coin,super_coin,pacman,portal,trash_can]
basic_buttons = [center,hamburger_open,hamburger_save,hamburger_play,hamburger_options,hamburger_leave,hamburger_leave,options_apply,options_reset]
hamburger_menu = [hamburger_container,hamburger_cross,hamburger_title,hamburger_open,hamburger_save,hamburger_play,hamburger_options,hamburger_leave]
options_menu = [options_container,options_cross,options_title,options_width,options_height,options_ghosts,options_apply,options_reset]

selected_block = None
hor_sym = False
ver_sym = False
user_dragging = False
user_placing = False
cur_menu = None

def loop(screen,new_winsize, dt, fps_infos, first_loop):

    global user_dragging

    if first_loop:
        json_files:list[str] = assets.get_save_files()
        for path in json_files:
            if path.endswith("latest.json"):
                save_manager.read(["map_editor","latest.json"])
                game_map.set_matrix(save_manager["matrix"])
                x = len(save_manager["matrix"][0:save_manager["matrix"].find("\n")])
                y = save_manager["matrix"].count("\n")
                if x > 30:
                    x = 30
                if x < 9:
                    x = 9
                if y > 30:
                    y = 30
                if y < 8:
                    y = 8
                options_width.set_option(str(x))
                options_height.set_option(str(y))
                options_ghosts.set_option(str(save_manager["nb_ghosts"]))
                break

    if fps_display.alive() != fps_infos[1]:
        if fps_infos[1]:
            fps_display.liven()
        else:
            fps_display.kill()
    fps_display_update.pass_time(dt)
    if fps_infos[1] and fps_display_update.finished:
        fps_display.set_text(f"max fps : {fps_infos[0]}\nfps : {1/dt:.2f}")
        fps_display_update.__init__(1)

    cursor = pygame.mouse.get_pos()
    cursor_offset = pygame.mouse.get_rel()

    hovered_clickable:Button|Image_button = (clickable_group.get_sprites_at(cursor) or [None])[-1]
    if hovered_clickable is not None:
        hovered_clickable.set_hovering(True)
    for btn in clickable_group.sprites():
        if btn is not hovered_clickable:
            btn.set_hovering(False)

    map_hover_manage(cursor)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in (pygame.BUTTON_LEFT,pygame.BUTTON_RIGHT):
                if hovered_clickable is not None:
                    hovered_clickable.set_clicking(True)
                elif (((event.button == pygame.BUTTON_LEFT and selected_block is None) or (not game_map.rect.collidepoint(cursor))) or event.button == pygame.BUTTON_RIGHT) and not buttons_container.rect.collidepoint(cursor) and not hamburger_container.rect.collidepoint(cursor):
                    user_dragging = True
                elif game_map.rect.collidepoint(cursor) and selected_block is not None and not hamburger_container.rect.collidepoint(cursor):
                    block_placing()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button in (pygame.BUTTON_LEFT,pygame.BUTTON_RIGHT): 
                if hovered_clickable is not None :
                    if hovered_clickable.clicking:
                        hovered_clickable.set_clicking(False)
                        return button_handling(hovered_clickable)
                for btn in clickable_group.sprites():
                    btn.set_clicking(False)
                user_dragging = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if cur_menu == None:
                    button_handling(hamburger)
                elif cur_menu == "hamburger":
                    button_handling(hamburger_cross)
                elif cur_menu == "options":
                    button_handling(options_cross)
            
        elif event.type == pygame.MOUSEWHEEL:
            game_map.change_size_index(event.y)
            for overlay in overlays:
                if overlay.alive():
                    overlay.set_size([game_map.tile_width-game_map.border_width]*2)
                else:
                    overlay.set_size([(game_map.tile_width-game_map.border_width)*assets.DEFAULT_WINSIZE[0]/game_map.winsize[0]]*2)
            kill_overlay()
    

    if user_dragging:
        x,y = [i*1.5 for i in cursor_offset]
        game_map.offset([x,0])
        if not game_map.rect.colliderect(background.rect):
            game_map.offset([-x,0])
        game_map.offset([0,y])
        if not game_map.rect.colliderect(background.rect):
            game_map.offset([0,-y])

    for btn in clickable_group.sprites():
        manage_states(btn)
    all_group.update(new_winsize,dt, cursor)
    to_draw_group.draw(screen)
    pygame.display.flip()


def manage_states(clickable:Image_button|Button|Slider):

    if not clickable.clicking_changed and not clickable.hovering_changed:
        return
    
    if clickable in hotbar:
        if not clickable.hovering and not clickable.clicking:
            clickable.instant_resize([clickable.resize_ratio,1],[0.15],['out']) #état de base du bouton
        elif clickable.hovering and not clickable.clicking:
            clickable.instant_resize([clickable.resize_ratio,0.95],[0.15],['out'])# état hover du bouton
        elif clickable.hovering and clickable.clicking:
            if clickable.clicking_changed and not clickable.hovering_changed:
                clickable.instant_resize([clickable.resize_ratio,0.9],[0.15],['in']) #état clicking du bouton
        elif not clickable.hovering and clickable.clicking:
            clickable.instant_resize([clickable.resize_ratio,0.9],[0.15],['in'])
            #état clicking du bouton

    elif clickable in basic_buttons:
        if not clickable.hovering and not clickable.clicking:
            clickable.instant_change_background_clr([clickable.background_clr[:],[250,250,250]],[0.25],["inout"])
            clickable.instant_change_border_width([clickable.border_width,2],[0.25],["inout"])
            if clickable is center:
                clickable.instant_change_border_padding([clickable.border_padding,1],[0.25],["inout"])
            else:
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

    elif clickable in [hamburger_cross,options_cross]:
        if not clickable.hovering and not clickable.clicking:
            clickable.instant_resize([clickable.resize_ratio,1],[0.15],['out']) #état de base du bouton
        elif clickable.hovering and not clickable.clicking:
            clickable.instant_resize([clickable.resize_ratio,0.95],[0.15],['out'])# état hover du bouton
        elif clickable.hovering and clickable.clicking:
            if clickable.clicking_changed and not clickable.hovering_changed:
                clickable.instant_resize([clickable.resize_ratio,0.85],[0.15],['in']) #état clicking du bouton
        elif not clickable.hovering and clickable.clicking:
            clickable.instant_resize([clickable.resize_ratio,0.85],[0.15],['in'])
            #état clicking du bouton

    elif type(clickable) is Slider:
        if not clickable.hovering and not clickable.clicking:
            clickable.instant_change_background_clr([clickable.background_clr[:],[250,250,250]],[0.25],['inout'])
        elif clickable.hovering and not clickable.clicking:
            clickable.instant_change_background_clr([clickable.background_clr[:],[230,230,230]],[0.25],['inout'])


def button_handling(button:Button|Image_button):
    global selected_block,hor_sym,ver_sym,cur_menu

    if button in hotbar_blocks:
        for btn in hotbar_blocks:
            btn.instant_change_border_width([button.border_width,1],[0],[])
        if button is not selected_block:
            button.instant_change_border_width([button.border_width,3],[0.25],['out'])
            selected_block = button
            if selected_block.name != block_overlay.name:
                block_overlay.set_name(selected_block.name)
                block_overlay_hor.set_name(selected_block.name)
                block_overlay_ver.set_name(selected_block.name)
                block_overlay_both.set_name(selected_block.name)
        else:
            selected_block = None

    elif button is horizontal_symetry:
        if hor_sym:
            button.instant_change_border_width([button.border_width,1],[0],[])
        else:
            button.instant_change_border_width([button.border_width,3],[0],[])
        hor_sym = not(hor_sym)
    
    elif button is vertical_symetry:
        if ver_sym:
            button.instant_change_border_width([button.border_width,1],[0],[])
        else:
            button.instant_change_border_width([button.border_width,3],[0],[])
        ver_sym = not(ver_sym)
    
    elif button is center:
        game_map.pos = [400*background.winsize[0]/assets.DEFAULT_WINSIZE[0],270*background.winsize[0]/assets.DEFAULT_WINSIZE[0]]
        game_map.calc_rect()

    elif button is hamburger:
        if cur_menu is None:
            cur_menu = "hamburger"
            show_hamburger()
        elif cur_menu == "hamburger":
            cur_menu = None
            hide_hamburger()
        elif cur_menu == "options":
            cur_menu = None
            hide_options()
            swap_menu_layers()

    elif button is hamburger_cross:
        cur_menu = None
        hide_hamburger()
    
    elif button is hamburger_open:
        path = assets.open_file_dialog()
        if path != "":
            data = JSON_handler(path)
            if len(data.data.keys()) == 3 and set(data.data.keys()) == {"matrix","nb_ghosts","date_of_creation"}:
                game_map.set_matrix(data["matrix"])
                save_manager["matrix"] = game_map.get_matrix()
                save_manager.save(["map_editor","latest.json"])
                button_handling(center)
                
    elif button is hamburger_save:
        path = assets.open_save_dialog()
        if path != "":
            save_manager.save(path)

    elif button is hamburger_play:
        return 1
        
    elif button is hamburger_options:
        cur_menu = "options"
        hide_hamburger()
        show_options()
        swap_menu_layers()

    elif button is options_cross:
        cur_menu = "hamburger"
        hide_options()
        show_hamburger()        
        swap_menu_layers()

    elif button is options_apply:
        dim = [game_map.x_tiles,game_map.y_tiles]
        change = False
        x = int(options_width.cur_option)
        y = int(options_height.cur_option)
        if x % 2 == 0:
            x += 1
        if y % 2 == 1:
            y += 1
        if x != dim[0]:
            change = True
            dim[0] = int(options_width.cur_option)
        if y != dim[1]:
            change = True
            dim[1] = int(options_height.cur_option)
        if change:
            print("signal")
            game_map.fill(dim)
            save_manager["matrix"] = game_map.get_matrix()
            button_handling(center)
        if int(options_ghosts.cur_option) != save_manager["nb_ghosts"]:
            save_manager["nb_ghosts"] = int(options_ghosts.cur_option)
        save_manager.save(["map_editor","latest.json"])
    
    elif button is options_reset:
        game_map.fill([game_map.x_tiles,game_map.y_tiles])
        save_manager["matrix"] = game_map.get_matrix()
        save_manager.save(["map_editor","latest.json"])
        button_handling(center)

    
    elif button is hamburger_leave:
        return 0

    kill_overlay()

def show_hamburger():
    positions = [[806.5,455],[620,108],[701,108],[701,193],[701,230],[701,267],[701,341],[701,378]]
    for elt,pos in zip(hamburger_menu,positions):
        elt.instant_translate([elt.pos,pos],[0.35],['out'])

def hide_hamburger():
    positions = [[1006.5,455],[820,108],[901,108],[901,193],[901,230],[901,267],[901,341],[901,378]]
    for elt,pos in zip(hamburger_menu,positions):
        elt.instant_translate([elt.pos,pos],[0.35],['in'])

def show_options():
    positions = [[806.5,455],[620,108],[701,108],[701,193],[701,230],[701,267],[701,341],[701,378]]
    for elt,pos in zip(options_menu,positions):
        elt.instant_translate([elt.pos,pos],[0.35],['out'])

def hide_options():
    positions = [[1006.5,455],[820,108],[901,108],[901,193],[901,230],[901,267],[901,341],[901,378]]
    for elt,pos in zip(options_menu,positions):
        elt.instant_translate([elt.pos,pos],[0.35],['in'])

def swap_menu_layers():
    for hamb,option in zip(hamburger_menu,options_menu):
            layer = to_draw_group.get_layer_of_sprite(option)
            to_draw_group.change_layer(option,to_draw_group.get_layer_of_sprite(hamb))
            to_draw_group.change_layer(hamb,layer)

def kill_overlay(overlay:Image|None = None):

    if overlay is None:
        for overlay in overlays:
            overlay.kill()
            translate_overlay(overlay,[0,0])
    else:
        overlay.kill()
        translate_overlay(overlay,[0,0])


def appear_overlay(overlay:Image|None = None):

    if overlay is None:
        for overlay in overlays:
            overlay.instant_change_alpha([0,175],[0.15],['in'])
        overlay.instant_resize([1.65,1,1.35,1],[0.15,0.075,0.075],['in','out','in'])
    else:
        overlay.instant_change_alpha([0,175],[0.15],['in'])
        overlay.instant_resize([1.65,1,1.35,1],[0.15,0.075,0.075],['in','out','in'])


def translate_overlay(overlay:Image,dest):

    if type(dest) not in (list,tuple):
        overlay.instant_translate([[0,0],game_map.get_abs_center(dest)],[0],[],False)
    else:
        overlay.instant_translate([[0,0],dest],[0],[],False)


def block_placing():

    for overlay in overlays:
        if overlay.alive():
            if selected_block is wall:
                game_map.set_tile_value(game_map.locate_tile(overlay.pos),"■") 
            elif selected_block is coin:
                game_map.set_tile_value(game_map.locate_tile(overlay.pos),".") 
            elif selected_block is super_coin:
                game_map.set_tile_value(game_map.locate_tile(overlay.pos),"●")
            elif selected_block is pacman:
                game_map.set_tile_value(game_map.locate_tile(overlay.pos),"P")
            elif selected_block is portal:
                if overlay.name == assets.GME_VALUE_TO_NAMES["→"]:
                    game_map.set_tile_value(game_map.locate_tile(overlay.pos),"→")
                else:
                    game_map.set_tile_value(game_map.locate_tile(overlay.pos),"←")
            elif game_map.locate_tile(overlay.pos).value in ["→","←"]:
                game_map.set_tile_value(game_map.locate_tile(overlay.pos),"X")
            elif game_map.locate_tile(overlay.pos).value in ["■",".","●"]:
                game_map.set_tile_value(game_map.locate_tile(overlay.pos),"□")
    save_manager["matrix"] = game_map.get_matrix()
    save_manager.save(["map_editor","latest.json"])


def map_hover_manage(cursor):

    if not game_map.rect.collidepoint(cursor) or user_dragging or center.hovering:
        kill_overlay()
    else:
        tile = game_map.locate_tile(cursor)
        if selected_block in [wall,coin,super_coin]:
            if tile.value == "□":
                if block_overlay.pos != game_map.get_abs_center(tile):
                    appear_overlay(block_overlay)
                    translate_overlay(block_overlay,tile)
                    if hor_sym and game_map.symetric_tile(tile,"x").value == "□":
                        appear_overlay(block_overlay_hor)
                        translate_overlay(block_overlay_hor,game_map.symetric_tile(tile,"x"))
                    else:
                        kill_overlay(block_overlay_hor)
                    if ver_sym and game_map.symetric_tile(tile,"y").value == "□":
                        appear_overlay(block_overlay_ver)
                        translate_overlay(block_overlay_ver,game_map.symetric_tile(tile,"y"))
                    else:
                        kill_overlay(block_overlay_ver)
                    if hor_sym and ver_sym and game_map.symetric_tile(tile).value == "□":
                        appear_overlay(block_overlay_both)
                        translate_overlay(block_overlay_both,game_map.symetric_tile(tile))
                    else:
                        kill_overlay(block_overlay_both)
                    if game_map.search_tile(tile)[1] == game_map.x_tiles//2:
                        kill_overlay(block_overlay_hor)
                        kill_overlay(block_overlay_both)
                elif not block_overlay.alive():
                    appear_overlay(block_overlay)
                    if hor_sym and game_map.symetric_tile(tile,"x").value == "□":
                        appear_overlay(block_overlay_hor)
                    else:
                        kill_overlay(block_overlay_hor)
                    if ver_sym and game_map.symetric_tile(tile,"y").value == "□":
                        appear_overlay(block_overlay_ver)
                    else:
                        kill_overlay(block_overlay_ver)
                    if hor_sym and ver_sym and game_map.symetric_tile(tile).value == "□":
                        appear_overlay(block_overlay_both)
                    else:
                        kill_overlay(block_overlay_both)
                    if game_map.search_tile(tile)[1] == game_map.x_tiles//2:
                        kill_overlay(block_overlay_hor)
                        kill_overlay(block_overlay_both)
            else:
                kill_overlay()

        elif selected_block is pacman:
            if tile.value == "□":
                if block_overlay.pos != game_map.get_abs_center(tile):
                    appear_overlay(block_overlay)
                    translate_overlay(block_overlay,tile)
                elif not block_overlay.alive():
                    appear_overlay(block_overlay)
            else:
                kill_overlay()

        elif selected_block is portal:
            pos = game_map.search_tile(tile)
            if pos[1]==0 and (["textures","left_portal.png"] in [block_overlay_hor.name,block_overlay_both.name] or ["textures","right_portal.png"] in [block_overlay.name,block_overlay_ver.name]):
                block_overlay.set_name(["textures","left_portal.png"])
                block_overlay_hor.set_name(["textures","right_portal.png"])
                block_overlay_ver.set_name(["textures","left_portal.png"])
                block_overlay_both.set_name(["textures","right_portal.png"])
            if pos[1]!=0 and (["textures","left_portal.png"] in [block_overlay.name,block_overlay_ver.name] or ["textures","right_portal.png"] in [block_overlay_hor.name,block_overlay_both.name]):
                block_overlay.set_name(["textures","right_portal.png"])
                block_overlay_hor.set_name(["textures","left_portal.png"])
                block_overlay_ver.set_name(["textures","right_portal.png"])
                block_overlay_both.set_name(["textures","left_portal.png"])
            if pos[1] in [0,game_map.x_tiles-1] and pos[0] not in [0,game_map.y_tiles-1] and tile.value == "X":
                if block_overlay.pos != game_map.get_abs_center(tile):
                    appear_overlay(block_overlay)
                    appear_overlay(block_overlay_hor)
                    translate_overlay(block_overlay,tile)
                    translate_overlay(block_overlay_hor,game_map.symetric_tile(tile,"x"))
                    if ver_sym and game_map.symetric_tile(tile,"y").value == "X":
                        appear_overlay(block_overlay_ver)
                        appear_overlay(block_overlay_both)
                        translate_overlay(block_overlay_ver,game_map.symetric_tile(tile,"y"))
                        translate_overlay(block_overlay_both,game_map.symetric_tile(tile))
                    else:
                        kill_overlay(block_overlay_ver)
                        kill_overlay(block_overlay_both)
                elif not block_overlay.alive():
                    appear_overlay(block_overlay)
                    appear_overlay(block_overlay_hor)
                    if ver_sym and game_map.symetric_tile(tile,"y").value == "X":
                        appear_overlay(block_overlay_ver)
                        appear_overlay(block_overlay_both)
                    else:
                        kill_overlay(block_overlay_ver)
                        kill_overlay(block_overlay_both)
            else:
                kill_overlay()

        elif selected_block is trash_can:
            if tile.value in ["■",".","●"]:
                for value in ["■",".","●"]:
                    if tile.value == value:
                        if block_overlay.pos != game_map.get_abs_center(tile):
                            appear_overlay(block_overlay)
                            translate_overlay(block_overlay,tile)
                            if hor_sym and game_map.symetric_tile(tile,"x").value == value:
                                appear_overlay(block_overlay_hor)
                                translate_overlay(block_overlay_hor,game_map.symetric_tile(tile,"x"))
                            else:
                                kill_overlay(block_overlay_hor)
                            if ver_sym and game_map.symetric_tile(tile,"y").value == value:
                                appear_overlay(block_overlay_ver)
                                translate_overlay(block_overlay_ver,game_map.symetric_tile(tile,"y"))
                            else:
                                kill_overlay(block_overlay_ver)
                            if hor_sym and ver_sym and game_map.symetric_tile(tile).value == value:
                                appear_overlay(block_overlay_both)
                                translate_overlay(block_overlay_both,game_map.symetric_tile(tile))
                            else:
                                kill_overlay(block_overlay_both)
                            if game_map.search_tile(tile)[1] == game_map.x_tiles//2:
                                kill_overlay(block_overlay_hor)
                                kill_overlay(block_overlay_both)
                        elif not block_overlay.alive():
                            appear_overlay(block_overlay)
                            if hor_sym and game_map.symetric_tile(tile,"x").value == value:
                                appear_overlay(block_overlay_hor)
                            else:
                                kill_overlay(block_overlay_hor)
                            if ver_sym and game_map.symetric_tile(tile,"y").value == value:
                                appear_overlay(block_overlay_ver)
                            else:
                                kill_overlay(block_overlay_ver)
                            if hor_sym and ver_sym and game_map.symetric_tile(tile).value == value:
                                appear_overlay(block_overlay_both)
                            else:
                                kill_overlay(block_overlay_both)
                            if game_map.search_tile(tile)[1] == game_map.x_tiles//2:
                                kill_overlay(block_overlay_hor)
                                kill_overlay(block_overlay_both)
                        break
            elif tile.value in ["←","→"]:
                if block_overlay.pos != game_map.get_abs_center(tile):
                    appear_overlay(block_overlay)
                    appear_overlay(block_overlay_hor)
                    translate_overlay(block_overlay,tile)
                    translate_overlay(block_overlay_hor,game_map.symetric_tile(tile,"x"))
                    if ver_sym and game_map.symetric_tile(tile,"y").value in ["←","→"]:
                        appear_overlay(block_overlay_ver)
                        appear_overlay(block_overlay_both)
                        translate_overlay(block_overlay_ver,game_map.symetric_tile(tile,"y"))
                        translate_overlay(block_overlay_both,game_map.symetric_tile(tile))
                    else:
                        kill_overlay(block_overlay_ver)
                        kill_overlay(block_overlay_both)
                elif not block_overlay.alive():
                    appear_overlay(block_overlay)
                    appear_overlay(block_overlay_hor)
                    if ver_sym and game_map.symetric_tile(tile,"y").value in ["←","→"]:
                        appear_overlay(block_overlay_ver)
                        appear_overlay(block_overlay_both)
                    else:
                        kill_overlay(block_overlay_ver)
                        kill_overlay(block_overlay_both)
            else:
                kill_overlay()
                        