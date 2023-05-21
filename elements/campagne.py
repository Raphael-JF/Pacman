"""
Ce module contient les éléments et widgets du menu de campagne. Il contient aussi le code de gestion utilisateur pour ce menu.
"""

import pygame,sys,assets
pygame.init()
from classes.box import Box
from classes.button import Button
from classes.title import Title
from classes.timer import Timer
from classes.json_handler import JSON_handler
from classes.image import Image

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
    background_clr = (242,242,242),
    size = [250 ,50],
    border=[2,(25,25,25),0,"inset"],
    text = "Campagne",
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
    text = "Retour",
    font_clrs=[(25,25,25)],
    font_size=30,
    font_family="RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group,clickable_group]
)

reset = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [(750,400),"midright"],
    background_clr = (250,250,250),
    size = [100,30],
    border=[2,(25,25,25),2,"inset"],
    text = "Réinitialiser",
    font_clrs=[(25,25,25)],
    font_size=20,
    font_family="RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group,clickable_group]
)

lvl1 = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [(140,150),"center"],
    background_clr = (250,250,250),
    size = [70,70],
    border=[2,(25,25,25),2,"inset"],
    text = "1",
    font_clrs=[(25,25,25)],
    font_size=35,
    font_family="RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group,clickable_group]
)

lock1 = Image(
    name = ["textures","padlock.png"],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [70,'x'],
    loc = [[140,150],"center"],
    border = [-1,[0,0,0],0,"inset"],
    layer = 2,
    parent_groups = [all_group, to_draw_group],
    living = False
)

lvl2 = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [(270,150),"center"],
    background_clr = (250,250,250),
    size = [70,70],
    border=[2,(25,25,25),2,"inset"],
    text = "2",
    font_clrs=[(25,25,25)],
    font_size=35,
    font_family="RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group,clickable_group]
)

lock2 = Image(
    name = ["textures","padlock.png"],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [70,'x'],
    loc = [[270,150],"center"],
    border = [-1,[0,0,0],0,"inset"],
    layer = 2,
    parent_groups = [all_group, to_draw_group],
    living = False
)

lvl3 = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [(400,150),"center"],
    background_clr = (250,250,250),
    size = [70,70],
    border=[2,(25,25,25),2,"inset"],
    text = "3",
    font_clrs=[(25,25,25)],
    font_size=35,
    font_family="RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group,clickable_group]
)

lock3 = Image(
    name = ["textures","padlock.png"],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [70,'x'],
    loc = [(400,150),"center"],
    border = [-1,[0,0,0],0,"inset"],
    layer = 2,
    parent_groups = [all_group, to_draw_group],
    living = False
)

lvl4 = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [(530,150),"center"],
    background_clr = (250,250,250),
    size = [70,70],
    border=[2,(25,25,25),2,"inset"],
    text = "4",
    font_clrs=[(25,25,25)],
    font_size=35,
    font_family="RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group,clickable_group]
)

lock4 = Image(
    name = ["textures","padlock.png"],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [70,'x'],
    loc = [(530,150),"center"],
    border = [-1,[0,0,0],0,"inset"],
    layer = 2,
    parent_groups = [all_group, to_draw_group],
    living = False
)

lvl5 = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [(660,150),"center"],
    background_clr = (250,250,250),
    size = [70,70],
    border=[2,(25,25,25),2,"inset"],
    text = "5",
    font_clrs=[(25,25,25)],
    font_size=35,
    font_family="RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group,clickable_group]
)

lock5 = Image(
    name = ["textures","padlock.png"],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [70,'x'],
    loc = [(660,150),"center"],
    border = [-1,[0,0,0],0,"inset"],
    layer = 2,
    parent_groups = [all_group, to_draw_group],
    living = False
)

lvl6 = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [(140,300),"center"],
    background_clr = (250,250,250),
    size = [70,70],
    border=[2,(25,25,25),2,"inset"],
    text = "6",
    font_clrs=[(25,25,25)],
    font_size=35,
    font_family="RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group,clickable_group]
)

lock6 = Image(
    name = ["textures","padlock.png"],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [70,'x'],
    loc = [(140,300),"center"],
    border = [-1,[0,0,0],0,"inset"],
    layer = 2,
    parent_groups = [all_group, to_draw_group],
    living = False
)

lvl7 = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [(270,300),"center"],
    background_clr = (250,250,250),
    size = [70,70],
    border=[2,(25,25,25),2,"inset"],
    text = "7",
    font_clrs=[(25,25,25)],
    font_size=35,
    font_family="RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group,clickable_group]
)

lock7 = Image(
    name = ["textures","padlock.png"],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [70,'x'],
    loc = [(270,300),"center"],
    border = [-1,[0,0,0],0,"inset"],
    layer = 2,
    parent_groups = [all_group, to_draw_group],
    living = False
)

lvl8 = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [(400,300),"center"],
    background_clr = (250,250,250),
    size = [70,70],
    border=[2,(25,25,25),2,"inset"],
    text = "8",
    font_clrs=[(25,25,25)],
    font_size=35,
    font_family="RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group,clickable_group]
)

lock8 = Image(
    name = ["textures","padlock.png"],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [70,'x'],
    loc = [(400,300),"center"],
    border = [-1,[0,0,0],0,"inset"],
    layer = 2,
    parent_groups = [all_group, to_draw_group],
    living = False
)

lvl9 = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [(530,300),"center"],
    background_clr = (250,250,250),
    size = [70,70],
    border=[2,(25,25,25),2,"inset"],
    text = "9",
    font_clrs=[(25,25,25)],
    font_size=35,
    font_family="RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group,clickable_group]
)

lock9 = Image(
    name = ["textures","padlock.png"],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [70,'x'],
    loc = [(530,300),"center"],
    border = [-1,[0,0,0],0,"inset"],
    layer = 2,
    parent_groups = [all_group, to_draw_group],
    living = False
)

lvl10 = Button(
    winsize=assets.DEFAULT_WINSIZE,
    loc = [(660,300),"center"],
    background_clr = (250,250,250),
    size = [70,70],
    border=[2,(25,25,25),2,"inset"],
    text = "10",
    font_clrs=[(25,25,25)],
    font_size=35,
    font_family="RopaSans-Regular.ttf",
    layer = 1,
    parent_groups = [all_group,to_draw_group,clickable_group]
)

lock10 = Image(
    name = ["textures","padlock.png"],
    winsize = assets.DEFAULT_WINSIZE,
    scale_axis = [70,'x'],
    loc = [(660,300),"center"],
    border = [-1,[0,0,0],0,"inset"],
    layer = 2,
    parent_groups = [all_group, to_draw_group],
    living = False
)

levels = [lvl1,lvl2,lvl3,lvl4,lvl5,lvl6,lvl7,lvl8,lvl9,lvl10]
locks = [lock1,lock2,lock3,lock4,lock5,lock6,lock7,lock8,lock9,lock10]
basic_buttons = [annuler,reset,lvl1,lvl2,lvl3,lvl4,lvl5,lvl6,lvl7,lvl8,lvl9,lvl10]

save_manager = JSON_handler()
data = assets.get_progress()
if data:
    save_manager.read(data)
else:
    assets.reset_progress(save_manager)
for key,value in save_manager.data.items():
    index = int(key[3:]) - 1 
    if not value:
        locks[index].liven()
        basic_buttons.remove(levels[index])










def loop(screen,new_winsize, dt,fps_infos):

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
                if hovered_clickable is not None :
                    if hovered_clickable.clicking:
                        res = button_handling(hovered_clickable)
                for btn in clickable_group.sprites():
                    btn.set_clicking(False)
                return res
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return 0
    
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

    if button not in basic_buttons:
        return

    if button is annuler:
        return 0
    
    elif button is reset:
        assets.reset_progress(save_manager)
        return 1
    
    elif button is lvl1:
        return "1"
    
    elif button is lvl2:
        return "2"
    
    elif button is lvl3:
        return "3"
    
    elif button is lvl4:
        return "4"
    
    elif button is lvl5:
        return "5"
    
    elif button is lvl6:
        return "6"
    
    elif button is lvl7:
        return "7"
    
    elif button is lvl8:
        return "8"
    
    elif button is lvl9:
        return "9"
    
    elif button is lvl10:
        return "10"
