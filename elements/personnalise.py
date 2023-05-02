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

all_group = pygame.sprite.Group()
to_draw_group = pygame.sprite.LayeredUpdates()
clickable_group = pygame.sprite.LayeredUpdates()
fps_display_update = Timer(0,'')

background = Box(
    winsize = assets.BASE_SIZE,
    size = [802,452],
    loc = [[0,0],"topleft"],
    background_clr=(17, 19, 166),
    border = [-1,(0,0,0),0,"inset"],
    parent_groups = [all_group, to_draw_group],
    layer = 0
)

fps_display = Title(
    winsize = assets.BASE_SIZE, 
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

buttons_container = Box(
    winsize = assets.BASE_SIZE,
    size = [806,92],
    loc = [[-3,-3],"topleft"],
    background_clr = [0,0,0,75],
    parent_groups = [all_group,to_draw_group],
    border = [3,[240,240,240],0,'inset'],
    layer = 1 
)

wall = Image_button(
    name = ['textures','wall.png'],
    winsize = assets.BASE_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[42.75,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 2
)

coin = Image_button(
    name = ['textures','coin.png'],
    winsize = assets.BASE_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[123.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 2
)

super_coin = Image_button(
    name = ['textures','super_coin.png'],
    winsize = assets.BASE_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[203.75,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 2
)

pacman = Image_button(
    name = ['textures','pacman','pacman_40.png'],
    winsize = assets.BASE_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[284.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 2
)

portal = Image_button(
    name = ['textures','right_portal.png'],
    winsize = assets.BASE_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[364.75,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 2
)

trash_can = Image_button(
    name = ['textures','trash_can.png'],
    winsize = assets.BASE_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[445.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 2
)

placement_options_selector = Box(
    winsize = assets.BASE_SIZE,
    size = [75.5,75.5],
    loc = [[0,0],"center"],
    background_clr = [255,255,255,75],
    parent_groups = [all_group,to_draw_group],
    border = [-1,[0,0,0],0,'inset'],
    layer = 3,
    living = False
)

placement_options = [wall,coin,super_coin,pacman,portal,trash_can]

separator = Box(
    winsize = assets.BASE_SIZE,
    size = [2,62.5],
    loc = [[520.75,42.75],'center'],
    background_clr = [0,0,0,75],
    parent_groups = [all_group,to_draw_group],
    border = [3,[215,215,215],0,'inset'],
    layer = 1 
)

horizontal_symetry = Image_button(
    name = ['textures','horizontal_symetry.png'],
    winsize = assets.BASE_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[596.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 2
)

vertical_symetry = Image_button(
    name = ['textures','vertical_symetry.png'],
    winsize = assets.BASE_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[676.75,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 2
)

hamburger = Image_button(
    name = ['textures','hamburger.png'],
    winsize = assets.BASE_SIZE,
    scale_axis = [75.5,'x'],
    loc = [[757.25,42.75],'center'],
    border = [1,[240,240,240],0,"inset"],
    parent_groups = [all_group,to_draw_group,clickable_group],
    layer = 2
)

hotbar = [wall,coin,super_coin,pacman,portal,trash_can,horizontal_symetry,vertical_symetry,hamburger]


last_hovered:Button|Image_button = None
def loop(screen,new_winsize, dt, fps_infos):

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

    hovered_button:Button|Image_button = (clickable_group.get_sprites_at(cursor) or [None])[-1]
    hover_manage(hovered_button)

    all_group.update(new_winsize,dt, cursor)
    to_draw_group.draw(screen)
    pygame.display.flip()
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in (pygame.BUTTON_LEFT,pygame.BUTTON_RIGHT):
                if hovered_button != None :
                    click_manage(hovered_button,True)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button in (pygame.BUTTON_LEFT,pygame.BUTTON_RIGHT): 
                if hovered_button != None :
                    if hovered_button.clicking:
                        res = button_handling(hovered_button)
                        click_manage(hovered_button,False)
                        return res
                for button in clickable_group.sprites():
                    button.set_clicking(False)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return 0


def hover_manage(button:Button|Image_button|None):

    global last_hovered

    if button is None:
        if last_hovered in hotbar:
            last_hovered.instant_resize([last_hovered.resize_ratio,1],[0.15],['out'])
        
    elif button != last_hovered:
        if last_hovered in hotbar:
            last_hovered.instant_resize([last_hovered.resize_ratio,1],[0.15],['out'])
        if button in hotbar:
            button.instant_resize([button.resize_ratio,0.95],[0.15],['in'])
    
    last_hovered = button


def click_manage(button:Button|Image_button,clicking:bool):

    update = False
    if button.clicking != clicking:
        update = True
        button.set_clicking(clicking)

    if update:
        print("signal")
        if clicking:
            if button in hotbar:
                button.instant_resize([button.resize_ratio,0.9],[0.15],['in'])
        else:
            if button in hotbar:
                # if button.hovering
                button.instant_resize([button.resize_ratio,1],[0.15],['out'])


def button_handling(button:Button|Image_button):

    if button in hotbar:
        # placement_options_selector.liven()
        # placement_options_selector.instant_translate([button.pos]*2,[0],['linear'])
        # placement_options_selector.instant_resize([button.resize_ratio]*2,[0],['linear'])
        button.instant_change_border_width([button.border_width,3],[0],['linear'])
