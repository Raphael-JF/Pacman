"""
Ce module contient les éléments et widgets du menu de campagne. Il contient aussi le code de gestion utilisateur pour ce menu.
"""

import pygame,sys,assets
pygame.init()
from classes.box import Box
from classes.button import Button
from classes.title import Title


all_group = pygame.sprite.Group()
to_draw_group = pygame.sprite.LayeredUpdates()
clickable_group = pygame.sprite.LayeredUpdates()

background = Box(
    winsize = assets.BASE_SIZE,
    size = [802,452],
    loc = [[0,0],"topleft"],
    background_clr=(9, 11, 89),
    border = [-1,(0,0,0),0,"inset"],
    parent_groups = [all_group, to_draw_group],
)

title = Title(
    winsize = assets.BASE_SIZE, 
    loc = [(400,25),"midtop"], 
    background_clr = (235,235,235),
    size = [250 ,50],
    border=[2,(25,25,25),0,"inset"],
    text = "Nouvelle partie",
    font_clrs = [(25,25,25)],
    font_size = 40,
    font_family = "RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group]
)

annuler = Button(
    winsize=assets.BASE_SIZE,
    loc = [(400,400),"center"],
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

reset = Button(
    winsize=assets.BASE_SIZE,
    loc = [(795,5),"topright"],
    background_clr = (250,250,250),
    size = [235,40],
    border=[2,(25,25,25),2,"inset"],
    text = "Réinitialiser",
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

lvl1 = Button(
    winsize=assets.BASE_SIZE,
    loc = [(140,225),"center"],
    background_clr = (250,250,250),
    size = [70,70],
    border=[2,(25,25,25),2,"inset"],
    text = "1",
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

lvl2 = Button(
    winsize=assets.BASE_SIZE,
    loc = [(270,225),"center"],
    background_clr = (250,250,250),
    size = [70,70],
    border=[2,(25,25,25),2,"inset"],
    text = "2",
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

lvl3 = Button(
    winsize=assets.BASE_SIZE,
    loc = [(400,225),"center"],
    background_clr = (250,250,250),
    size = [70,70],
    border=[2,(25,25,25),2,"inset"],
    text = "3",
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

lvl4 = Button(
    winsize=assets.BASE_SIZE,
    loc = [(530,225),"center"],
    background_clr = (250,250,250),
    size = [70,70],
    border=[2,(25,25,25),2,"inset"],
    text = "4",
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

lvl5 = Button(
    winsize=assets.BASE_SIZE,
    loc = [(660,225),"center"],
    background_clr = (250,250,250),
    size = [70,70],
    border=[2,(25,25,25),2,"inset"],
    text = "5",
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

    if button is annuler:
        return 1