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
    winsize = assets.DEFAULT_SIZE,
    size = [802,452],
    loc = [[0,0],"topleft"],
    background_clr=(17, 19, 166),
    border = [-1,(0,0,0),0,"inset"],
    parent_groups = [all_group, to_draw_group],
    layer = 0
)

fps_display = Title(
    winsize = assets.DEFAULT_SIZE, 
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

game_map = Game_map_editor(
    winsize = assets.DEFAULT_SIZE,
    dimensions = assets.GME_DEFAULT_DIMENSIONS,
    scale_axis = [300,'y'],
    loc = [[400,270],"center"],
    background_clr = [0,0,0,0],
    parent_groups = [all_group,to_draw_group],
    living = True,
    layer = 2
)

block_overlay = Image(
    winsize = assets.DEFAULT_SIZE,
    name = ["textures","empty_tile.png"],
    scale_axis = [game_map.tile_width,'x'],
    loc = [[0,0],"center"],
    border = [-1,[0,0,0],0,'inset'],
    parent_groups = [all_group,to_draw_group],
    layer = 3,
    living = False
)
block_overlay_horizontal = Image(
    winsize = assets.DEFAULT_SIZE,
    name = ["textures","empty_tile.png"],
    scale_axis = [game_map.tile_width,'x'],
    loc = [[0,0],"center"],
    border = [-1,[0,0,0],0,'inset'],
    parent_groups = [all_group,to_draw_group],
    layer = 3,
    living = False
)

block_overlay_vertical = Image(
    winsize = assets.DEFAULT_SIZE,
    name = ["textures","empty_tile.png"],
    scale_axis = [game_map.tile_width,'x'],
    loc = [[0,0],"center"],
    border = [-1,[0,0,0],0,'inset'],
    parent_groups = [all_group,to_draw_group],
    layer = 3,
    living = False
)

block_overlay_both = Image(
    winsize = assets.DEFAULT_SIZE,
    name = ["textures","empty_tile.png"],
    scale_axis = [game_map.tile_width,'x'],
    loc = [[0,0],"center"],
    border = [-1,[0,0,0],0,'inset'],
    parent_groups = [all_group,to_draw_group],
    layer = 3,
    living = False
)
block_overlay.set_size([game_map.tile_width-game_map.border_width]*2)
block_overlay_horizontal.set_size([game_map.tile_width-game_map.border_width]*2)
block_overlay_vertical.set_size([game_map.tile_width-game_map.border_width]*2)
block_overlay_both.set_size([game_map.tile_width-game_map.border_width]*2)

buttons_container = Box(
    winsize = assets.DEFAULT_SIZE,
    size = [806,92],
    loc = [[-3,-3],"topleft"],
    background_clr = [0,0,0,75],
    parent_groups = [all_group,to_draw_group],
    border = [3,[240,240,240],0,'inset'],
    layer = 3 
)

wall = Image_button(
    name = ['textures','wall.png'],
    winsize = assets.DEFAULT_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[42.75,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 4
)

coin = Image_button(
    name = ['textures','coin.png'],
    winsize = assets.DEFAULT_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[123.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 4
)

super_coin = Image_button(
    name = ['textures','super_coin.png'],
    winsize = assets.DEFAULT_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[203.75,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 4
)

pacman = Image_button(
    name = ['textures','pacman','pacman_40.png'],
    winsize = assets.DEFAULT_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[284.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 4
)

portal = Image_button(
    name = ['textures','right_portal.png'],
    winsize = assets.DEFAULT_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[364.75,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 4
)

trash_can = Image_button(
    name = ['textures','trash_can.png'],
    winsize = assets.DEFAULT_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[445.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 4
)

placement_options = [wall,coin,super_coin,pacman,portal,trash_can]

separator = Box(
    winsize = assets.DEFAULT_SIZE,
    size = [2,62.5],
    loc = [[520.75,42.75],'center'],
    background_clr = [0,0,0,75],
    parent_groups = [all_group,to_draw_group],
    border = [3,[215,215,215],0,'inset'],
    layer = 4
)

horizontal_symetry = Image_button(
    name = ['textures','horizontal_symetry.png'],
    winsize = assets.DEFAULT_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[596.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 4
)

vertical_symetry = Image_button(
    name = ['textures','vertical_symetry.png'],
    winsize = assets.DEFAULT_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[676.75,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 4
)

hamburger = Image_button(
    name = ['textures','hamburger.png'],
    winsize = assets.DEFAULT_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[757.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 4
)

overlays = [block_overlay,block_overlay_horizontal,block_overlay_vertical,block_overlay_both]
hotbar = [wall,coin,super_coin,pacman,portal,trash_can,horizontal_symetry,vertical_symetry,hamburger]
hotbar_blocks = [wall,coin,super_coin,pacman,portal,trash_can]
selected_block = None
hor_sym = False
ver_sym = False
user_dragging = False

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
                if not buttons_container.rect.collidepoint(cursor):
                    if (event.button == pygame.BUTTON_LEFT and selected_block is None) or not game_map.rect.collidepoint(cursor):
                        block_overlay.kill()
                        block_overlay_horizontal.kill()
                        block_overlay_vertical.kill()
                        block_overlay_both.kill()
                        user_dragging = True
                    if event.button == pygame.BUTTON_RIGHT:
                        block_overlay.kill()
                        block_overlay_horizontal.kill()
                        block_overlay_vertical.kill()
                        block_overlay_both.kill()
                        user_dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button in (pygame.BUTTON_LEFT,pygame.BUTTON_RIGHT): 
                if hovered_clickable is not None :
                    if hovered_clickable.clicking:
                        hovered_clickable.set_clicking(False)
                        return button_handling(hovered_clickable)
                for btn in clickable_group.sprites():
                    btn.set_clicking(False)
                if event.button == pygame.BUTTON_LEFT:
                    user_dragging = False
                if event.button == pygame.BUTTON_RIGHT:
                    user_dragging = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return 0
            
        elif event.type == pygame.MOUSEWHEEL:
            game_map.change_size_index(event.y)
            block_overlay.set_size([game_map.tile_width-game_map.border_width]*2)
            block_overlay_horizontal.set_size([game_map.tile_width-game_map.border_width]*2)
            block_overlay_vertical.set_size([game_map.tile_width-game_map.border_width]*2)
            block_overlay_both.set_size([game_map.tile_width-game_map.border_width]*2)
            kill_overlays()
    
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


def manage_states(button:Image_button):

    if not button.clicking_changed and not button.hovering_changed:
        return
    
    if button in hotbar:
        if not button.hovering and not button.clicking:
            button.instant_resize([button.resize_ratio,1],[0.15],['out'])
        elif button.hovering and not button.clicking:
            button.instant_resize([button.resize_ratio,0.95],[0.15],['out'])
        elif button.hovering and button.clicking:
            if button.clicking_changed and not button.hovering_changed:
                button.instant_resize([button.resize_ratio,0.9],[0.15],['in'])
        elif not button.hovering and button.clicking:
            button.instant_resize([button.resize_ratio,0.9],[0.15],['in'])


def button_handling(button:Button|Image_button):
    global selected_block,hor_sym,ver_sym

    if button in hotbar_blocks:
        for btn in hotbar_blocks:
            btn.instant_change_border_width([button.border_width,1],[0],[])
        if button is not selected_block:
            button.instant_change_border_width([button.border_width,3],[0.25],['out'])
            selected_block = button
            if selected_block.name != block_overlay.name:
                block_overlay.set_name(selected_block.name)
                block_overlay_horizontal.set_name(selected_block.name)
                block_overlay_vertical.set_name(selected_block.name)
                block_overlay_both.set_name(selected_block.name)
                if button is portal:
                    block_overlay_horizontal.set_name(["textures","left_portal.png"])
                    block_overlay_both.set_name(["textures","left_portal.png"])
                    
        else:
            selected_block = None

    if button is horizontal_symetry:
        if hor_sym:
            button.instant_change_border_width([button.border_width,1],[0],[])
        else:
            button.instant_change_border_width([button.border_width,3],[0],[])
        hor_sym = not(hor_sym)
        for overlay in overlays:
            overlay.instant_translate([[0,0],[0,0]],[0],[],False)
    
    if button is vertical_symetry:
        if ver_sym:
            button.instant_change_border_width([button.border_width,1],[0],[])
        else:
            button.instant_change_border_width([button.border_width,3],[0],[])
        ver_sym = not(ver_sym)
        for overlay in overlays:
            overlay.instant_translate([[0,0],[0,0]],[0],[],False)
    
    kill_overlays()


def kill_overlays():
    
    for overlay in overlays:
        overlay.kill()

def appear_overlay(overlay:Image):

    overlay.instant_change_alpha([0,175],[0.15],['in'])
    overlay.instant_resize([1.65,1],[0.15],['in'])

def map_hover_manage(cursor):

    if not game_map.rect.collidepoint(cursor) or user_dragging:
        kill_overlays()
    else:
        tile = game_map.get_tile(cursor)
        if selected_block in [wall,coin,super_coin]:
            if tile.value == "□":
                if block_overlay.pos != game_map.get_abs_center(tile):
                    appear_overlay(block_overlay)
                    block_overlay.instant_translate([[0,0],game_map.get_abs_center(tile)],[0],[],False)
                    if hor_sym and game_map.symetric_tile(tile,"x").value == "□":
                        appear_overlay(block_overlay_horizontal)
                        block_overlay_horizontal.instant_translate([[0,0],game_map.get_abs_center(game_map.symetric_tile(tile,"x"))],[0],[],False)
                    else:
                        block_overlay_horizontal.kill()
                    if ver_sym and game_map.symetric_tile(tile,"y").value == "□":
                        appear_overlay(block_overlay_vertical)
                        block_overlay_vertical.instant_translate([[0,0],game_map.get_abs_center(game_map.symetric_tile(tile,"y"))],[0],[],False)
                    else:
                        block_overlay_vertical.kill()
                    if hor_sym and ver_sym and game_map.symetric_tile(tile).value == "□":
                        appear_overlay(block_overlay_both)
                        block_overlay_both.instant_translate([[0,0],game_map.get_abs_center(game_map.symetric_tile(tile))],[0],[],False)
                    else:
                        block_overlay_both.kill()
                    if game_map.search_tile(tile)[1] == game_map.x_tiles//2 or game_map.symetric_tile(tile,"y").value != "□":
                        block_overlay_horizontal.kill()
                        block_overlay_both.kill()
                        block_overlay_vertical.kill()
                elif not block_overlay.alive():
                    appear_overlay(block_overlay)
                    if hor_sym and game_map.symetric_tile(tile,"x").value == "□":
                        appear_overlay(block_overlay_horizontal)
                    else:
                        block_overlay_horizontal.kill()
                    if ver_sym and game_map.symetric_tile(tile,"y").value == "□":
                        appear_overlay(block_overlay_vertical)
                    else:
                        block_overlay_vertical.kill()
                    if hor_sym and ver_sym and game_map.symetric_tile(tile).value == "□":
                        appear_overlay(block_overlay_both)
                    else:
                        block_overlay_both.kill()
                    if game_map.search_tile(tile)[1] == game_map.x_tiles//2:
                        block_overlay_horizontal.kill()
                        block_overlay_both.kill()
            else:
                kill_overlays()

        elif selected_block is pacman:
            if tile.value == "□":
                if block_overlay.pos != game_map.get_abs_center(tile):
                    appear_overlay(block_overlay)
                    block_overlay.instant_translate([[0,0],game_map.get_abs_center(tile)],[0],[],False)
                elif not block_overlay.alive():
                    appear_overlay(block_overlay)
            else:
                kill_overlays()

        elif selected_block is portal:
            pos = game_map.search_tile(tile)
            if pos[1]==0 and block_overlay.name == ["textures","right_portal.png"]:
                block_overlay.set_name(["textures","left_portal.png"])
                block_overlay_horizontal.set_name(["textures","right_portal.png"])
                block_overlay_vertical.set_name(["textures","left_portal.png"])
                block_overlay_both.set_name(["textures","right_portal.png"])
            elif pos[1]!=0 and block_overlay.name == ["textures","left_portal.png"]:
                block_overlay.set_name(["textures","right_portal.png"])
                block_overlay_horizontal.set_name(["textures","left_portal.png"])
                block_overlay_vertical.set_name(["textures","right_portal.png"])
                block_overlay_both.set_name(["textures","left_portal.png"])
            if pos[1] in [0,game_map.x_tiles-1] and pos[0] not in [0,game_map.y_tiles-1] and tile.value == "X":
                if block_overlay.pos != game_map.get_abs_center(tile):
                    appear_overlay(block_overlay)
                    appear_overlay(block_overlay_horizontal)
                    block_overlay_horizontal.instant_translate([[0,0],game_map.get_abs_center(game_map.symetric_tile(tile,"x"))],[0],[],False)
                    block_overlay.instant_translate([[0,0],game_map.get_abs_center(tile)],[0],[],False)
                    if ver_sym and game_map.symetric_tile(tile,"y").value == "X":
                        appear_overlay(block_overlay_vertical)
                        appear_overlay(block_overlay_both)
                        block_overlay_vertical.instant_translate([[0,0],game_map.get_abs_center(game_map.symetric_tile(tile,"y"))],[0],[],False)
                        block_overlay_both.instant_translate([[0,0],game_map.get_abs_center(game_map.symetric_tile(tile))],[0],[],False)
                    else:
                        block_overlay_vertical.kill()
                        block_overlay_both.kill()
                elif not block_overlay.alive():
                    appear_overlay(block_overlay)
                    appear_overlay(block_overlay_horizontal)
                    if ver_sym and game_map.symetric_tile(tile,"y").value == "X":
                        appear_overlay(block_overlay_vertical)
                        appear_overlay(block_overlay_both)
                    else:
                        block_overlay_vertical.kill()
                        block_overlay_both.kill()
            else:
                kill_overlays()