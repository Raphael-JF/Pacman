import assets,pygame,os
from classes.image import Image


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
            # name = ["textures","pacman","pacman_40.png"],
            name = ["textures","r.png"],
            winsize = winsize,
            scale_axis = [width,"x"],
            loc = [topleft,"topleft"],
            parent_groups = [group],
            border = [-1,[0,0,0,0],0,"inset"],
            layer = 2
        )
        self.next = {
            "top" : None,
            "bottom" : None,
            "right" : None,
            "left" : None,
        }
        self.direction = None
    

    def get_next_rect(self,dt):

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