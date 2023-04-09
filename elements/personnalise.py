"""
Ce module contient les éléments et widgets du menu de campagne. Il contient aussi le code de gestion utilisateur pour ce menu.
"""

import pygame,sys,assets
pygame.init()
from classes.box import Box
from classes.button import Button
from classes.title import Title
from classes.slider import Slider

all_group = pygame.sprite.Group()
to_draw_group = pygame.sprite.LayeredUpdates()
clickable_group = pygame.sprite.LayeredUpdates()

background = Box(
    winsize = assets.BASE_SIZE,
    size = [802,452],
    loc = [[0,0],"topleft"],
    background_clr=(17, 19, 166),
    border = [-1,(0,0,0),0,"inset"],
    parent_groups = [all_group, to_draw_group],
)

title = Title(
    winsize = assets.BASE_SIZE, 
    loc = [(400,20),"midtop"], 
    background_clr = (235,235,235),
    size = [250 ,50],
    border=[2,(25,25,25),0,"inset"],
    text = "Personnalisé",
    font_clrs = [(25,25,25)],
    font_size = 40,
    font_family = "RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group]
)

test1 = Slider(
    winsize = assets.BASE_SIZE,
    loc = [(187.5,127.4),"center"],
    font_clrs=[(25,25,25)],
    parent_groups= [all_group, to_draw_group, clickable_group],
    font_size=30,
    size = [205,35],
    options_list = ['1','2','3','4','5','6','7','8','9','10'],
    base_option = '4',
    cursor_width = 15,
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
    text = "fantômes : {}",
    font_family = "RopaSans-Regular.ttf",
    layer = 5,
    living = True
)

jouer = Button(
    winsize=assets.BASE_SIZE,
    loc = [(180,260),"center"],
    background_clr = (250,250,250),
    size = [80,20],
    border=[2,(25,25,25),2,"inset"],
    text = "random",
    font_clrs=[(25,25,25)],
    font_size=20,
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

zone_parametres = Box(
    winsize = assets.BASE_SIZE,
    loc = [(187.5,225),'center'],
    size = [275,280],
    background_clr = (25, 29, 255),
    border = [4,(17, 19, 166),4,"inset"],
    layer = 1,
    parent_groups = [all_group,to_draw_group]
)

zone_preview = Box(
    winsize = assets.BASE_SIZE,
    loc = [(555,225),'center'],
    size = [390,280],
    background_clr = (25, 29, 255),
    border = [4,(17, 19, 166),4,"inset"],
    layer = 1,
    parent_groups = [all_group,to_draw_group]
)


reset = Button(
    winsize=assets.BASE_SIZE,
    loc = [(475,405),"center"],
    background_clr = (250,250,250),
    size = [120,40],
    border=[2,(25,25,25),2,"inset"],
    text = "reset",
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

jouer = Button(
    winsize=assets.BASE_SIZE,
    loc = [(655,405),"center"],
    background_clr = (250,250,250),
    size = [120,40],
    border=[2,(25,25,25),2,"inset"],
    text = "Jouer",
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

retour = Button(
    winsize=assets.BASE_SIZE,
    loc = [(180,405),"center"],
    background_clr = (250,250,250),
    size = [135,40],
    border=[2,(25,25,25),2,"inset"],
    text = "Retour",
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



def loop(screen,new_winsize, dt,fps):

    cursor = pygame.mouse.get_pos()

    hovered_button:Button = (clickable_group.get_sprites_at(cursor) or [None])[-1]

    all_group.update(new_winsize,dt,fps,cursor)
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

    if button is retour:
        return 1