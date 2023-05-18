"""
Ce module contient les éléments et widgets du menu de campagne. Il contient aussi le code de gestion utilisateur pour ce menu.
"""

import pygame,sys,assets
pygame.init()
from classes.timer import Timer
from classes.box import Box
from classes.button import Button
from classes.title import Title


all_group = pygame.sprite.Group()
to_draw_group = pygame.sprite.LayeredUpdates()
clickable_group = pygame.sprite.LayeredUpdates()
fps_display_update = Timer(0)

background = Box(
    winsize = assets.DEFAULT_WINSIZE,
    size = [802,452],
    loc = [[0,0],"topleft"],
    background_clr=(17, 19, 166),
    border = [-1,(0,0,0),0,"inset"],
    parent_groups = [all_group, to_draw_group],
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

title = Title(
    winsize = assets.DEFAULT_WINSIZE, 
    loc = [(400,25),"midtop"], 
    background_clr = (235,235,235),
    size = [250 ,50],
    border=[2,(25,25,25),0,"inset"],
    text = "Crédits",
    font_clrs = [(25,25,25)],
    font_size = 40,
    font_family = "RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group]
)

annuler = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [(400,400),"center"],
    background_clr = (250,250,250),
    size = [235,40],
    border=[2,(25,25,25),2,"inset"],
    text = "Annuler",
    font_clrs=[(25,25,25)],
    font_size=30,
    font_family="RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group,clickable_group]
)

basic_buttons = [annuler]




def loop(screen,new_winsize, dt, fps_infos):

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
    
    for btn in clickable_group.sprites():
        manage_states(btn)
    all_group.update(new_winsize,dt,cursor)
    to_draw_group.draw(screen)
    pygame.display.flip()


def manage_states(button:Button):
    
    if not button.clicking_changed and not button.hovering_changed:
        return
    
    if button in basic_buttons:
        if not button.hovering and not button.clicking:
            button.instant_change_background_clr([button.background_clr[:],[250,250,250]],[0.25],["inout"])
            button.instant_change_border_width([button.border_width,2],[0.25],["inout"])
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

def button_handling(button:Button):

    if button is annuler:
        return 0