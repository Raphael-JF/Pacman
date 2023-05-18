import assets,pygame,os
from classes.image import Image
from classes.timer import Timer


class Empty_cell(Image):

    def __init__(self,winsize,topleft,width,group):

        super().__init__(
            name = ["textures","empty_tile.png"],
            winsize = winsize,
            scale_axis = [width,"x"],
            loc = [topleft,"topleft"],
            parent_groups = [group],
            border = [-1,[0,0,0,0],0,"inset"],
            layer = 0
        )
        self.next = {
            "top" : None,
            "bottom" : None,
            "right" : None,
            "left" : None
        }


class Wall(Image):

    def __init__(self,winsize,topleft,width,group):

        super().__init__(
            name = ["textures","wall.png"],
            winsize = winsize,
            scale_axis = [width,"x"],
            loc = [topleft,"topleft"],
            parent_groups = [group],
            border = [-1,[0,0,0,0],0,"inset"],
            layer = 1
        )
        self.next = {
            "top" : None,
            "bottom" : None,
            "right" : None,
            "left" : None
        }


class Ghost_door(Image):

    def __init__(self,winsize,topleft,width,group):

        super().__init__(
            name = ["textures","ghost_door.png"],
            winsize = winsize,
            scale_axis = [width,"x"],
            loc = [topleft,"topleft"],
            parent_groups = [group],
            border = [-1,[0,0,0,0],0,"inset"],
            layer = 1
        )
        self.next = {
            "top" : None,
            "bottom" : None,
            "right" : None,
            "left" : None
        }



class Coin(Image):

    def __init__(self,winsize,topleft,width,group):

        super().__init__(
            name = ["textures","coin.png"],
            winsize = winsize,
            scale_axis = [width,"x"],
            loc = [topleft,"topleft"],
            parent_groups = [group],
            border = [-1,[0,0,0,0],0,"inset"],
            layer = 1
        )
        self.next = {
            "top" : None,
            "bottom" : None,
            "right" : None,
            "left" : None
        }

class Super_coin(Image):

    def __init__(self,winsize,topleft,width,group):

        super().__init__(
            name = ["textures","super_coin.png"],
            winsize = winsize,
            scale_axis = [width,"x"],
            loc = [topleft,"topleft"],
            parent_groups = [group],
            border = [-1,[0,0,0,0],0,"inset"],
            layer = 1
        )
        self.next = {
            "top" : None,
            "bottom" : None,
            "right" : None,
            "left" : None
        }

class Pacman(Image):

    def __init__(self,winsize,topleft,width,group):

        super().__init__(
            name = ["textures","pacman","pacman_40.png"],
            winsize = winsize,
            scale_axis = [width,"x"],
            loc = [topleft,"topleft"],
            parent_groups = [group],
            border = [-1,[0,0,0,0],0,"inset"],
            layer = 10
        )
        self.next = {
            "top" : None,
            "bottom" : None,
            "right" : None,
            "left" : None,
        }
        self.direction = None
        self.next_direction = None
        self.sprite_sheets = []
        self.moving_anim_timer = Timer(assets.SPRITES_DELAY,self.animate_moving)
        self.animate_moving()

    def update(self,dt):

        if self.direction is not None:
            self.moving_anim_timer.pass_time(dt)


    def animate_moving(self):
        
        if len(self.sprite_sheets) == 0:
            self.sprite_sheets = [["textures","pacman","pacman_0.png"],["textures","pacman","pacman_20.png"],["textures","pacman","pacman_40.png"],["textures","pacman","pacman_60.png"],["textures","pacman","pacman_80.png"],["textures","pacman","pacman_60.png"],["textures","pacman","pacman_40.png"],["textures","pacman","pacman_20.png"]]
        self.set_name(self.sprite_sheets.pop(0))
        self.moving_anim_timer = Timer(assets.SPRITES_DELAY,self.animate_moving)


    def set_direction(self,new_dir):

        if self.direction != new_dir:
            self.direction = new_dir
            if self.direction == "top":
                self.degrees = 90
            elif self.direction == "left":
                self.degrees = 180
            elif self.direction == "bottom":
                self.degrees = 270
            elif self.direction == "right":
                self.degrees = 0
            self.calc_image()
        

    

    def get_next_rect(self,dt):

        print(assets.PACMAN_SPEED(self.width)*dt)

        offset = [0,0]
        if self.direction is not None:
            match self.direction:
                case "top":
                    offset[1] -= assets.PACMAN_SPEED(self.width)*dt
                case "bottom":
                    offset[1] += assets.PACMAN_SPEED(self.width)*dt
                case "left":
                    offset[0] -= assets.PACMAN_SPEED(self.width)*dt
                case "right":
                    offset[0] += assets.PACMAN_SPEED(self.width)*dt
        return self.rect.move(*offset)