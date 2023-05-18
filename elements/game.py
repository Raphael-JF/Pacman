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

game_map = None

cells:list[Image] = []


def loop(screen,new_winsize, dt, new_lvl_path, fps_infos):
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
            winsize = assets.DEFAULT_WINSIZE,
            loc = [[400,225],"center"],
            lvl_path = new_lvl_path,
            size = [800,450],
            parent_groups = [all_group,to_draw_group]

        )

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
                return 0
            elif event.key in [pygame.K_UP,pygame.K_z]:
                game_map.handle_input("top")
            elif event.key in [pygame.K_DOWN,pygame.K_s]:
                game_map.handle_input("bottom")
            elif event.key in [pygame.K_LEFT,pygame.K_q]:
                game_map.handle_input("left")
            elif event.key in [pygame.K_RIGHT,pygame.K_d]:
                game_map.handle_input("right")
            
    
    for btn in clickable_group.sprites():
        manage_states(btn)
    all_group.update(new_winsize,dt,cursor)
    to_draw_group.draw(screen)
    pygame.display.flip()

def manage_states(btn):
    pass

def button_handling(clickable:Button):
    pass


    
    