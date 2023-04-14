"""
Ce module contient les éléments et widgets du menu de campagne. Il contient aussi le code de gestion utilisateur pour ce menu.
"""

import pygame,sys,assets
pygame.init()
from classes.timer import Timer
from classes.box import Box
from classes.button import Button
from classes.title import Title
from classes.slider import Slider


all_group = pygame.sprite.Group()
to_draw_group = pygame.sprite.LayeredUpdates()
clickable_group = pygame.sprite.LayeredUpdates()
fps_display_update = Timer(0,'')

background = Box(
    winsize = assets.BASE_SIZE,
    size = [800,450],
    loc = [[0,0],"topleft"],
    background_clr=(17, 19, 166),
    border = [-1,(0,0,0),0,"inset"],
    parent_groups = [all_group, to_draw_group],
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

title = Title(
    winsize = assets.BASE_SIZE, 
    loc = [(400,25),"midtop"], 
    background_clr = (235,235,235),
    size = [250 ,50],
    border=[2,(25,25,25),0,"inset"],
    text = "Options",
    font_clrs = [(25,25,25)],
    font_size = 40,
    font_family = "RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group]
)

resolution = Slider(
    winsize = assets.BASE_SIZE,
    loc = [(216,150),"center"],
    font_clrs=[(25,25,25)],
    parent_groups= [all_group, to_draw_group, clickable_group],
    font_size=30,
    size = [300,40],
    options_list = [f'{i}x{j}' for i,j in assets.GAME_RESOLUTIONS],
    base_option = '{}x{}'.format(*assets.GAME_RESOLUTIONS[0]),
    cursor_width = 22.5,
    background_clr= (250,250,250),
    hov_background_clr=(230,230,230),
    cursor_background_clr=(175,175,175),
    hov_cursor_background_clr=(175,175,175),
    cursor_border = [2,(20,20,20)],
    hov_cursor_border = [2,(20,20,20)],
    border = [2,(20,20,20),0,"inset"],
    hov_border=[2,(20,20,20),0],
    ease_seconds = 0.25,
    ease_mode = "inout",
    text = "Résolution : {}",
    font_family = "RopaSans-Regular.ttf",
    layer = 5,
    living = True
)

rafraichissement = Slider(
    winsize = assets.BASE_SIZE,
    loc = [(584,150),"center"],
    font_clrs=[(25,25,25)],
    parent_groups= [all_group, to_draw_group, clickable_group],
    font_size=30,
    size = [300,40],
    options_list = [str(i) for i in range(10,250,10)],
    base_option = '60',
    cursor_width = 22.5,
    background_clr= (250,250,250),
    hov_background_clr=(230,230,230),
    cursor_background_clr=(175,175,175),
    hov_cursor_background_clr=(175,175,175),
    cursor_border = [2,(20,20,20)],
    hov_cursor_border = [2,(20,20,20)],
    border = [2,(20,20,20),0,"inset"],
    hov_border=[2,(20,20,20),0],
    ease_seconds = 0.25,
    ease_mode = "inout",
    text = "Rafraîchissement : {} fps",
    font_family = "RopaSans-Regular.ttf",
    layer = 5,
    living = True
)

montrer_fps = Button(
    winsize=assets.BASE_SIZE,
    loc = [(584,210),"center"],
    background_clr = (250,250,250),
    size = [300,40],
    border=[2,(25,25,25),2,"inset"],
    text = "Montrer les fps : Non",
    font_clrs=[(25,25,25)],
    font_size=30,
    font_family="RopaSans-Regular.ttf",
    ease_seconds=0.25,
    ease_mode="inout",
    hov_background_clr=(230,230,230),
    hov_border=[2,(25,25,25),0],
    active_background_clr=(210,210,210),
    active_border=[3,(25,25,25),0],
    layer = 1,
    parent_groups = [all_group,to_draw_group,clickable_group]  
)

annuler = Button(
    winsize=assets.BASE_SIZE,
    loc = [(250,400),"center"],
    background_clr = (250,250,250),
    size = [235,40],
    border=[2,(25,25,25),2,"inset"],
    text = "Annuler",
    font_clrs=[(25,25,25)],
    font_size=30,
    font_family="RopaSans-Regular.ttf",
    ease_seconds=0.25,
    ease_mode="inout",
    hov_background_clr=(230,230,230),
    hov_border=[2,(25,25,25),0],
    active_background_clr=(210,210,210),
    active_border=[3,(25,25,25),0],
    layer = 1,
    parent_groups = [all_group,to_draw_group,clickable_group]
)

appliquer = Button(
    winsize=assets.BASE_SIZE,
    loc = [(550,400),"center"],
    background_clr = (250,250,250),
    size = [235,40],
    border=[2,(25,25,25),2,"inset"],
    text = "Appliquer",
    font_clrs=[(25,25,25)],
    font_size=30,
    font_family="RopaSans-Regular.ttf",
    ease_seconds=0.25,
    ease_mode="inout",
    hov_background_clr=(230,230,230),
    hov_border=[2,(25,25,25),0],
    active_background_clr=(210,210,210),
    active_border=[3,(25,25,25),0],
    layer = 1,
    parent_groups = [all_group,to_draw_group,clickable_group]
)


def loop(screen,new_winsize, dt, fps_infos, first_looping):

    if first_looping :
        resolution.set_option(f"{new_winsize[0]}x{new_winsize[1]}")
        rafraichissement.set_option(str(fps_infos[0]))
        if fps_infos[1]:
            montrer_fps.set_text("Montrer les fps : Oui")
        else:
            montrer_fps.set_text("Montrer les fps : Non")

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

    hovered_button:Button = (clickable_group.get_sprites_at(cursor) or [None])[-1]

    all_group.update(new_winsize,dt,cursor)
    to_draw_group.draw(screen)
    pygame.display.flip()
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button in (pygame.BUTTON_LEFT,pygame.BUTTON_RIGHT):
                if hovered_button != None :
                    hovered_button.set_clicking(True)

        elif event.type == pygame.MOUSEBUTTONUP:

            if event.button in (pygame.BUTTON_LEFT,pygame.BUTTON_RIGHT): 
                if hovered_button != None :
                    if hovered_button.clicking:
                        res = click_manage(hovered_button)
                        hovered_button.set_clicking(False)
                        return res
                        
                for button in clickable_group.sprites():
                    button.set_clicking(False)


def click_manage(button:Button):

    if button is annuler :
        return 0
    
    elif button is appliquer :
        return {'resolution' : [int(i) for i in resolution.cur_option.split('x')],
                'fps' : int(rafraichissement.cur_option),
                'montrer_fps' : montrer_fps.texte == "Montrer les fps : Oui"}

    elif button is montrer_fps :
        if montrer_fps.texte == "Montrer les fps : Non":
            montrer_fps.set_text("Montrer les fps : Oui")
        else:
            montrer_fps.set_text("Montrer les fps : Non")