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

    def __init__(self,winsize,topleft,width,game_map,group):

        super().__init__(
            name = ["textures","pacman","pacman_40.png"],
            winsize = winsize,
            scale_axis = [width,"x"],
            loc = [topleft,"topleft"],
            parent_groups = [group],
            border = [-1,[0,0,0,0],0,"inset"],
            layer = 2
        )
        self.game_map = game_map
        self.direction = None
        self.next_direction = None
        self.group = group
        self.sprite_sheets = []
        self.moving_anim_timer = Timer(assets.SPRITES_DELAY,self.animate_moving)
        self.animate_moving()

    def update(self,dt):

        if self.direction is not None:
            self.moving_anim_timer.pass_time(dt)
            old_pacman_rect = self.rect
            self.rect = self.get_next_rect(dt)
            self.path(old_pacman_rect)
            self.check_walls()

        a = self.game_map.locate_pos
        if self.direction == "top":
            print(a([self.rect.centerx,self.rect.top+1]))
        if self.direction == "bottom":
            print(a([self.rect.centerx,self.rect.bottom-1]))
        if self.direction == "left":
            print(a([self.rect.left+1,self.rect.centery]))
        if self.direction == "right":
            print(a([self.rect.right-1,self.rect.centery]))


    def animate_moving(self):
        
        if len(self.sprite_sheets) == 0:
            self.sprite_sheets = [["textures","pacman","pacman_0.png"],["textures","pacman","pacman_20.png"],["textures","pacman","pacman_40.png"],["textures","pacman","pacman_60.png"],["textures","pacman","pacman_80.png"],["textures","pacman","pacman_60.png"],["textures","pacman","pacman_40.png"],["textures","pacman","pacman_20.png"]]
        self.set_name(self.sprite_sheets.pop(0))
        self.moving_anim_timer = Timer(assets.SPRITES_DELAY,self.animate_moving)


    def set_direction(self,new_dir):

        import time
        self.test = time.perf_counter()
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
        return self.rect.move(offset)


    def path(self,old_pacman_rect):

        if self.next_direction is not None:
            cell_width = round(self.width) + round(self.width) % 2
            if self.direction == "top":
                old_top = old_pacman_rect.top
                new_top = self.rect.top
                fixed_y = old_top - old_top%cell_width
                if old_top  >= fixed_y >=  new_top and type(self.game_map.locate_cell(self.rect.center).next[self.next_direction]) in [Coin,Super_coin,Empty_cell]:
                    self.rect.top = fixed_y
                    if self.next_direction == "left":
                        self.rect.centerx -= old_top - new_top
                    else:
                        self.rect.centerx += old_top - new_top
                    self.set_direction(self.next_direction)
                    self.next_direction = None

            elif self.direction == "bottom":
                old_bottom = old_pacman_rect.bottom
                new_bottom = self.rect.bottom
                fixed_y = old_bottom+cell_width-old_bottom%cell_width
                if old_bottom  <= fixed_y <=  new_bottom and type(self.game_map.locate_cell(self.rect.center).next[self.next_direction]) in [Coin,Super_coin,Empty_cell]:
                    self.rect.bottom = fixed_y
                    if self.next_direction == "left":
                        self.rect.centerx -= new_bottom - old_bottom
                    else:
                        self.rect.centerx += new_bottom - old_bottom
                    self.set_direction(self.next_direction)
                    self.next_direction = None

            elif self.direction == "left":
                old_left = old_pacman_rect.left
                new_left = self.rect.left
                fixed_x = old_left - old_left%cell_width
                if old_left  >= fixed_x >=  new_left and type(self.game_map.locate_cell(self.rect.center).next[self.next_direction]) in [Coin,Super_coin,Empty_cell]:
                    self.rect.left = fixed_x
                    if self.next_direction == "top":
                        self.rect.centery -= old_left - new_left
                    else:
                        self.rect.centery += old_left - new_left
                    self.set_direction(self.next_direction)
                    self.next_direction = None

            elif self.direction == "right":
                old_right = old_pacman_rect.right
                new_right = self.rect.right
                fixed_x = old_right+cell_width-old_right%cell_width
                if old_right  <= fixed_x <=  new_right and type(self.game_map.locate_cell(self.rect.center).next[self.next_direction]) in [Coin,Super_coin,Empty_cell]:
                    self.rect.right = fixed_x
                    if self.next_direction == "top":
                        self.rect.centery -= new_right - old_right
                    else:
                        self.rect.centery += new_right - old_right
                    self.set_direction(self.next_direction)
                    self.next_direction = None


    def check_walls(self):

        colliding = pygame.sprite.spritecollide(self,self.group,False,lambda a,b :a.rect.colliderect(b.rect))
        walls = [sprite for sprite in colliding if isinstance(sprite, Wall) or isinstance(sprite,Ghost_door)]
        if walls:
            wall = walls[0]
            if self.direction == "top" and self.rect.top <= wall.rect.bottom:
                self.rect.top = wall.rect.bottom
            elif self.direction == "bottom" and self.rect.bottom >= wall.rect.top:
                self.rect.bottom = wall.rect.top
            elif self.direction == "left" and self.rect.left <= wall.rect.right:
                self.rect.left = wall.rect.right
            elif self.direction == "right" and self.rect.right >= wall.rect.left:
                self.rect.right = wall.rect.left
            self.direction = None
            self.next_direction = None

        cell_width = round(self.width) + round(self.width) % 2
        if self.rect.left > self.game_map.x_cells * cell_width:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = self.game_map.y_cells * cell_width
            






class Ghost(Image):

    def __init__(self,winsize,topleft,width,game_map,group):

        super().__init__(
            name = ["textures","ghost.png"],
            winsize = winsize,
            scale_axis = [width,"x"],
            loc = [topleft,"topleft"],
            parent_groups = [group],
            border = [-1,[0,0,0,0],0,"inset"],
            layer = 3
        )
        self.game_map = game_map
        self.direction = None
        self.next_direction = None
        self.group = group
        self.sprite_sheets = []
        self.moving_anim_timer = Timer(assets.SPRITES_DELAY,self.animate_moving)
        self.animate_moving()

    def update(self,dt):

        if self.direction is not None:
            self.moving_anim_timer.pass_time(dt)
            old_rect = self.rect
            self.rect = self.get_next_rect(dt)
            self.path(old_rect)
            self.check_walls()

        a = self.game_map.locate_pos
        if self.direction == "top":
            print(a([self.rect.centerx,self.rect.top+1]))
        if self.direction == "bottom":
            print(a([self.rect.centerx,self.rect.bottom-1]))
        if self.direction == "left":
            print(a([self.rect.left+1,self.rect.centery]))
        if self.direction == "right":
            print(a([self.rect.right-1,self.rect.centery]))


    def set_direction(self,new_dir):

        import time
        self.test = time.perf_counter()
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
        return self.rect.move(offset)


    def path(self,old_pacman_rect):

        if self.next_direction is not None:
            cell_width = round(self.width) + round(self.width) % 2
            if self.direction == "top":
                old_top = old_pacman_rect.top
                new_top = self.rect.top
                fixed_y = old_top - old_top%cell_width
                if old_top  >= fixed_y >=  new_top and type(self.game_map.locate_cell(self.rect.center).next[self.next_direction]) in [Coin,Super_coin,Empty_cell]:
                    self.rect.top = fixed_y
                    if self.next_direction == "left":
                        self.rect.centerx -= old_top - new_top
                    else:
                        self.rect.centerx += old_top - new_top
                    self.set_direction(self.next_direction)
                    self.next_direction = None

            elif self.direction == "bottom":
                old_bottom = old_pacman_rect.bottom
                new_bottom = self.rect.bottom
                fixed_y = old_bottom+cell_width-old_bottom%cell_width
                if old_bottom  <= fixed_y <=  new_bottom and type(self.game_map.locate_cell(self.rect.center).next[self.next_direction]) in [Coin,Super_coin,Empty_cell]:
                    self.rect.bottom = fixed_y
                    if self.next_direction == "left":
                        self.rect.centerx -= new_bottom - old_bottom
                    else:
                        self.rect.centerx += new_bottom - old_bottom
                    self.set_direction(self.next_direction)
                    self.next_direction = None

            elif self.direction == "left":
                old_left = old_pacman_rect.left
                new_left = self.rect.left
                fixed_x = old_left - old_left%cell_width
                if old_left  >= fixed_x >=  new_left and type(self.game_map.locate_cell(self.rect.center).next[self.next_direction]) in [Coin,Super_coin,Empty_cell]:
                    self.rect.left = fixed_x
                    if self.next_direction == "top":
                        self.rect.centery -= old_left - new_left
                    else:
                        self.rect.centery += old_left - new_left
                    self.set_direction(self.next_direction)
                    self.next_direction = None

            elif self.direction == "right":
                old_right = old_pacman_rect.right
                new_right = self.rect.right
                fixed_x = old_right+cell_width-old_right%cell_width
                if old_right  <= fixed_x <=  new_right and type(self.game_map.locate_cell(self.rect.center).next[self.next_direction]) in [Coin,Super_coin,Empty_cell]:
                    self.rect.right = fixed_x
                    if self.next_direction == "top":
                        self.rect.centery -= new_right - old_right
                    else:
                        self.rect.centery += new_right - old_right
                    self.set_direction(self.next_direction)
                    self.next_direction = None


    def check_walls(self):

        colliding = pygame.sprite.spritecollide(self,self.group,False,lambda a,b :a.rect.colliderect(b.rect))
        walls = [sprite for sprite in colliding if isinstance(sprite, Wall) or isinstance(sprite,Ghost_door)]
        if walls:
            wall = walls[0]
            if self.direction == "top" and self.rect.top <= wall.rect.bottom:
                self.rect.top = wall.rect.bottom
            elif self.direction == "bottom" and self.rect.bottom >= wall.rect.top:
                self.rect.bottom = wall.rect.top
            elif self.direction == "left" and self.rect.left <= wall.rect.right:
                self.rect.left = wall.rect.right
            elif self.direction == "right" and self.rect.right >= wall.rect.left:
                self.rect.right = wall.rect.left
            self.direction = None
            self.next_direction = None

        cell_width = round(self.width) + round(self.width) % 2
        if self.rect.left > self.game_map.x_cells * cell_width:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = self.game_map.y_cells * cell_width