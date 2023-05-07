"""
Ce module contient les éléments et widgets du menu de campagne. Il contient aussi le code de gestion utilisateur pour ce menu.
"""

import pygame,sys,assets
pygame.init()
from classes.timer import Timer
from classes.box import Box
from classes.button import Button
from classes.title import Title
from classes.image_button import Image_button
from classes.game_map_editor import Game_map_editor
from classes.image import Image

all_group = pygame.sprite.Group()
to_draw_group = pygame.sprite.LayeredUpdates()
clickable_group = pygame.sprite.LayeredUpdates()
fps_display_update = Timer(0,'')

background = Box(
    winsize = assets.DEFAULT_WINSIZE,
    size = [800,450],
    loc = [[0,0],"topleft"],
    background_clr=[7, 9, 83],
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
    scale_axis = [game_map.tile_width,'x'],
    loc = [[0,0],"center"],
    border = [-1,[0,0,0],0,'inset'],
    parent_groups = [all_group,to_draw_group],
    layer = 3,
    living = False
)
block_overlay_hor = Image(
    winsize = assets.DEFAULT_WINSIZE,
    name = ["textures","empty_tile.png"],
    scale_axis = [game_map.tile_width,'x'],
    loc = [[0,0],"center"],
    border = [-1,[0,0,0],0,'inset'],
    parent_groups = [all_group,to_draw_group],
    layer = 3,
    living = False
)

block_overlay_ver = Image(
    winsize = assets.DEFAULT_WINSIZE,
    name = ["textures","empty_tile.png"],
    scale_axis = [game_map.tile_width,'x'],
    loc = [[0,0],"center"],
    border = [-1,[0,0,0],0,'inset'],
    parent_groups = [all_group,to_draw_group],
    layer = 3,
    living = False
)

block_overlay_both = Image(
    winsize = assets.DEFAULT_WINSIZE,
    name = ["textures","empty_tile.png"],
    scale_axis = [game_map.tile_width,'x'],
    loc = [[0,0],"center"],
    border = [-1,[0,0,0],0,'inset'],
    parent_groups = [all_group,to_draw_group],
    layer = 3,
    living = False
)
block_overlay.set_size([game_map.tile_width-game_map.border_width]*2)
block_overlay_hor.set_size([game_map.tile_width-game_map.border_width]*2)
block_overlay_ver.set_size([game_map.tile_width-game_map.border_width]*2)
block_overlay_both.set_size([game_map.tile_width-game_map.border_width]*2)

buttons_container = Box(
    winsize = assets.DEFAULT_WINSIZE,
    size = [806,92],
    loc = [[-3,-3],"topleft"],
    background_clr = [0,0,0,200],
    parent_groups = [all_group,to_draw_group],
    border = [1.5,[175,175,175,200],0,'inset'],
    layer = 4 
)

wall = Image_button(
    name = ['textures','wall.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[42.75,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 5
)

coin = Image_button(
    name = ['textures','coin.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[123.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 5
)

super_coin = Image_button(
    name = ['textures','super_coin.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[203.75,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 5
)

pacman = Image_button(
    name = ['textures','pacman','pacman_40.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[284.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 5
)

portal = Image_button(
    name = ['textures','right_portal.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[364.75,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 5
)

trash_can = Image_button(
    name = ['textures','trash_can.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[445.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 5
)

placement_options = [wall,coin,super_coin,pacman,portal,trash_can]

separator = Box(
    winsize = assets.DEFAULT_WINSIZE,
    size = [2,62.5],
    loc = [[520.75,42.75],'center'],
    background_clr = [0,0,0,75],
    parent_groups = [all_group,to_draw_group],
    border = [3,[215,215,215],0,'inset'],
    layer = 5
)

horizontal_symetry = Image_button(
    name = ['textures','horizontal_symetry.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[596.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 5
)

vertical_symetry = Image_button(
    name = ['textures','vertical_symetry.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[676.75,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 5
)

hamburger = Image_button(
    name = ['textures','hamburger.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [75.5,'x'],
    loc = [[757.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 5
)

hamburger_container = Box(
    winsize = assets.DEFAULT_WINSIZE,
    loc = [[1006.5,455],"bottomright"],
    size = [205,366],
    background_clr = [0,0,0,200],
    parent_groups = [all_group,to_draw_group],
    border = [1.5,[175,175,175,200],0,'inset'],
    layer = 3
)

hamburger_cross = Image_button(
    name = ['textures','white_cross.png'],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [26,'x'],
    loc = [[820,108],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 4
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
    layer = 4,
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
    layer = 4,
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
    layer = 4,
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
    layer = 4,
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
    layer = 4,
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
    layer = 4,
    parent_groups = [all_group,to_draw_group,clickable_group]  
)



overlays = [block_overlay,block_overlay_hor,block_overlay_ver,block_overlay_both]
hotbar = [wall,coin,super_coin,pacman,portal,trash_can,horizontal_symetry,vertical_symetry,hamburger]
hotbar_blocks = [wall,coin,super_coin,pacman,portal,trash_can]
basic_buttons = [center,hamburger_open,hamburger_save,hamburger_play,hamburger_options,hamburger_leave,hamburger_leave]
hamburger_menu = [hamburger_container,hamburger_cross,hamburger_title,hamburger_open,hamburger_save,hamburger_play,hamburger_options,hamburger_leave]

selected_block = None
hor_sym = False
ver_sym = False
user_dragging = False
user_placing = False
cur_menu = None

def loop(screen,new_winsize, dt, fps_infos):

    global user_dragging

    if fps_display.alive() != fps_infos[1]:
        if fps_infos[1]:
            fps_display.liven()
        else:
            fps_display.kill()
    fps_display_update.pass_time(dt)
    if fps_infos[1] and fps_display_update.finished:
        fps_display.set_text(f"max fps : {fps_infos[0]}\nfps : {1/dt:.2f}")
        fps_display_update.__init__(1,'')

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
                elif (((event.button == pygame.BUTTON_LEFT and selected_block is None) or (not game_map.rect.collidepoint(cursor))) or event.button == pygame.BUTTON_RIGHT) and not buttons_container.rect.collidepoint(cursor):
                    user_dragging = True
                elif game_map.rect.collidepoint(cursor) and selected_block is not None:
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
                else:
                    button_handling(hamburger_cross)
            elif event.key == pygame.K_a:
                print(game_map.get_matrix())
            
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


def manage_states(button:Image_button|Button):

    if not button.clicking_changed and not button.hovering_changed:
        return
    
    if button in hotbar:
        if not button.hovering and not button.clicking:
            button.instant_resize([button.resize_ratio,1],[0.15],['out']) #état de base du bouton
        elif button.hovering and not button.clicking:
            button.instant_resize([button.resize_ratio,0.95],[0.15],['out'])# état hover du bouton
        elif button.hovering and button.clicking:
            if button.clicking_changed and not button.hovering_changed:
                button.instant_resize([button.resize_ratio,0.9],[0.15],['in']) #état clicking du bouton
        elif not button.hovering and button.clicking:
            button.instant_resize([button.resize_ratio,0.9],[0.15],['in'])
            #état clicking du bouton

    elif button in basic_buttons:
        if not button.hovering and not button.clicking:
            button.instant_change_background_clr([button.background_clr[:],[250,250,250]],[0.25],["inout"])
            button.instant_change_border_width([button.border_width,2],[0.25],["inout"])
            if button is center:
                button.instant_change_border_padding([button.border_padding,1],[0.25],["inout"])
            else:
                button.instant_change_border_padding([button.border_padding,2],[0.25],["inout"])
        elif button.hovering and not button.clicking:
            button.instant_change_background_clr([button.background_clr[:],[230,230,230]],[0.25],["inout"])
            button.instant_change_border_width([button.border_width,2],[0.25],["inout"])
            button.instant_change_border_padding([button.border_padding,0],[0.25],["inout"])
        elif button.hovering and button.clicking:
            if button.clicking_changed and not button.hovering_changed:
                button.instant_change_background_clr([button.background_clr[:],[210,210,210]],[0.25],["inout"])
                button.instant_change_border_width([button.border_width,3],[0.25],["inout"])
                button.instant_change_border_padding([button.border_padding,0],[0.25],["inout"])
        elif not button.hovering and button.clicking:
                button.instant_change_background_clr([button.background_clr[:],[210,210,210]],[0.25],["inout"])
                button.instant_change_border_width([button.border_width,3],[0.25],["inout"])
                button.instant_change_border_padding([button.border_padding,0],[0.25],["inout"])

    elif button is hamburger_cross:
        if not button.hovering and not button.clicking:
            button.instant_resize([button.resize_ratio,1],[0.15],['out']) #état de base du bouton
        elif button.hovering and not button.clicking:
            button.instant_resize([button.resize_ratio,0.95],[0.15],['out'])# état hover du bouton
        elif button.hovering and button.clicking:
            if button.clicking_changed and not button.hovering_changed:
                button.instant_resize([button.resize_ratio,0.85],[0.15],['in']) #état clicking du bouton
        elif not button.hovering and button.clicking:
            button.instant_resize([button.resize_ratio,0.85],[0.15],['in'])
            #état clicking du bouton


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
            positions = [[806.5,455],[620,108],[701,108],[701,193],[701,230],[701,267],[701,341],[701,378]]
            for elt,pos in zip(hamburger_menu,positions):
                elt.instant_translate([elt.pos,pos],[0.35],['out'])
        else:
            return button_handling(hamburger_cross)

    elif button is hamburger_cross:
        cur_menu = None
        positions = [[1006.5,455],[820,108],[901,108],[901,193],[901,230],[901,267],[901,341],[901,378]]
        for elt,pos in zip(hamburger_menu,positions):
            elt.instant_translate([elt.pos,pos],[0.35],['in'])
    
    elif button is hamburger_leave:
        return 0

    kill_overlay()


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
                game_map.set_tile_value(game_map.get_tile(overlay.pos),"■") 
            elif selected_block is coin:
                game_map.set_tile_value(game_map.get_tile(overlay.pos),".") 
            elif selected_block is super_coin:
                game_map.set_tile_value(game_map.get_tile(overlay.pos),"●")
            elif selected_block is pacman:
                game_map.set_tile_value(game_map.get_tile(overlay.pos),"P")
            elif selected_block is portal:
                if overlay.name == assets.GME_VALUE_TO_NAMES["→"]:
                    game_map.set_tile_value(game_map.get_tile(overlay.pos),"→")
                else:
                    game_map.set_tile_value(game_map.get_tile(overlay.pos),"←")
            elif game_map.get_tile(overlay.pos).value in ["→","←"]:
                game_map.set_tile_value(game_map.get_tile(overlay.pos),"X")
            elif game_map.get_tile(overlay.pos).value in ["■",".","●"]:
                game_map.set_tile_value(game_map.get_tile(overlay.pos),"□")

def map_hover_manage(cursor):

    if not game_map.rect.collidepoint(cursor) or user_dragging or center.hovering:
        kill_overlay()
    else:
        tile = game_map.get_tile(cursor)
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
                        