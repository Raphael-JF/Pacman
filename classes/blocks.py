import assets,pygame,random
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
        self.anim_timer = Timer(assets.SPRITES_DELAY,self.animate)
        self.animate()

    def update(self,dt):


        self.anim_timer.pass_time(dt)

        if self.direction is not None:
            old_pacman_rect = self.rect
            self.rect = self.get_next_rect(dt)
            self.path(old_pacman_rect)
            self.check_walls()


    def animate(self):
        
        self.anim_timer = Timer(assets.SPRITES_DELAY,self.animate)

        if self.direction is not None:
            if len(self.sprite_sheets) == 0:
                self.sprite_sheets = [["textures","pacman","pacman_0.png"],["textures","pacman","pacman_20.png"],["textures","pacman","pacman_40.png"],["textures","pacman","pacman_60.png"],["textures","pacman","pacman_80.png"],["textures","pacman","pacman_60.png"],["textures","pacman","pacman_40.png"],["textures","pacman","pacman_20.png"]]
            self.set_name(self.sprite_sheets.pop(0))
            
        


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


    def next_fixed_pos(self):

        a = self.game_map.locate_pos
        if self.direction == "top":
            return a([self.rect.centerx,self.rect.top+1])
        if self.direction == "bottom":
            return a([self.rect.centerx,self.rect.bottom-1])
        if self.direction == "left":
            return a([self.rect.left+1,self.rect.centery])
        if self.direction == "right":
            return a([self.rect.right-1,self.rect.centery])
        else:
            return a(self.rect.center)
        

    def path(self,old_pacman_rect):

        if self.next_direction is not None:
            cell_width = round(self.width) + round(self.width) % 2
            if self.direction == "top":
                old_top = old_pacman_rect.top
                new_top = self.rect.top
                fixed_y = old_top - old_top%cell_width
                if old_top  > fixed_y >=  new_top and type(self.game_map.locate_cell(self.rect.center).next[self.next_direction]) in [Coin,Super_coin,Empty_cell]:
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
                if old_bottom  < fixed_y <=  new_bottom and type(self.game_map.locate_cell(self.rect.center).next[self.next_direction]) in [Coin,Super_coin,Empty_cell]:
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
                if old_left  > fixed_x >=  new_left and type(self.game_map.locate_cell(self.rect.center).next[self.next_direction]) in [Coin,Super_coin,Empty_cell]:
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
                if old_right  < fixed_x <=  new_right and type(self.game_map.locate_cell(self.rect.center).next[self.next_direction]) in [Coin,Super_coin,Empty_cell]:
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
    """
    états possibles:
    - 'wandering'
    - 'imprisoned'
    - 'escaping'
    - 'chasing'
    """

    def __init__(self,winsize,color,speed,topleft,width,game_map,group):

        super().__init__(
            name = ["textures","ghost",color,"right","0.png"],
            # name = ['textures','r.png'],
            winsize = winsize,
            scale_axis = [width,"x"],
            loc = [topleft,"topleft"],
            parent_groups = [group],
            border = [-1,[0,0,0,0],0,"inset"],
            layer = 3
        )
        self.game_map = game_map
        self.color = color
        self.speed = speed
        self.direction = None
        self.next_moves = []
        self.group = group
        self.sprite_sheets = []
        self.state = "imprisoned"
        self.state_timer:Timer = None
        # self.anim_timer = Timer(assets.SPRITES_DELAY,self.animate)
        # self.animate()

    def update(self,dt):

        # self.anim_timer.pass_time(dt)
        if self.state_timer:
            self.state_timer.pass_time(dt)
        
        if self.state == "imprisoned":
            if len(self.next_moves) == 0:
                self.next_moves = ["top","bottom"]
            if self.direction is None:
                self.direction = self.next_moves.pop(0)
                
        elif self.state == "wandering":
            if len(self.next_moves) == 0:
                self.next_moves = ["left","right","bottom","top"]
                random.shuffle(self.next_moves)
                self.next_moves.pop(0)
            if self.direction is None:
                self.direction = self.next_moves.pop(0)

        elif self.state == "chasing":
            if len(self.next_moves) == 0:
                self.next_moves = self.game_map.get_moves(self.game_map.graph.dijkstra(self.next_fixed_pos(),self.game_map.pacman.next_fixed_pos()))
            if self.direction is None:
                try:
                    self.direction = self.next_moves.pop(0)
                except:
                    self.direction = random.choice(self.available_dir())



        if self.direction is not None:
            old_rect = self.rect
            self.rect = self.get_next_rect(dt)
            self.path(old_rect)
            self.check_walls()


    def get_next_rect(self,dt):

        offset = [0,0]
        if self.direction is not None:
            match self.direction:
                case "top":
                    offset[1] -= self.speed*self.width*dt
                case "bottom":
                    offset[1] += self.speed*self.width*dt
                case "left":
                    offset[0] -= self.speed*self.width*dt
                case "right":
                    offset[0] += self.speed*self.width*dt
        return self.rect.move(offset)


    def available_dir(self):
        
        cell = self.game_map.locate_cell(self.rect.center)
        res = []
        for dir,c in cell.next.items():
            if type(c) in [Empty_cell,Coin,Super_coin,Ghost_door]:
                res.append(dir)
        return res


    def next_fixed_pos(self):

        a = self.game_map.locate_pos
        if self.direction == "top":
            return a([self.rect.centerx,self.rect.top+1])
        elif self.direction == "bottom":
            return a([self.rect.centerx,self.rect.bottom-1])
        elif self.direction == "left":
            return a([self.rect.left+1,self.rect.centery])
        elif self.direction == "right":
            return a([self.rect.right-1,self.rect.centery])
        else:
            return a(self.rect.center)
        
    
    def set_state(self,state):
        
        if state == self.state:
            return
        
        elif state == "chasing":
            self.next_moves = []

        elif state == "wandering":
            self.next_moves = []
        self.state = state


    def path(self,old_rect:pygame.Rect):

        if len(self.next_moves) != 0:
            next_direction = self.next_moves[0]
            cell_width = round(self.width) + round(self.width) % 2
            if self.direction == "top":
                old_top = old_rect.top
                new_top = self.rect.top
                fixed_y = old_top - old_top%cell_width
                if old_top  > fixed_y >=  new_top and type(self.game_map.locate_cell(self.rect.center).next[next_direction]) in [Coin,Super_coin,Empty_cell,Ghost_door]:
                    self.rect.top = fixed_y
                    self.direction = self.next_moves.pop(0)
                    if next_direction == "left":
                        self.rect.centerx -= old_top - new_top
                    elif next_direction == "right":
                        self.rect.centerx += old_top - new_top

            elif self.direction == "bottom":
                old_bottom = old_rect.bottom
                new_bottom = self.rect.bottom
                fixed_y = old_bottom+cell_width-old_bottom%cell_width
                if old_bottom  < fixed_y <=  new_bottom and type(self.game_map.locate_cell(self.rect.center).next[next_direction]) in [Coin,Super_coin,Empty_cell,Ghost_door]:
                    self.rect.bottom = fixed_y
                    self.direction = self.next_moves.pop(0)
                    if next_direction == "left":
                        self.rect.centerx -= new_bottom - old_bottom
                    elif next_direction == "right":
                        self.rect.centerx += new_bottom - old_bottom

            elif self.direction == "left":
                old_left = old_rect.left
                new_left = self.rect.left
                fixed_x = old_left - old_left%cell_width
                if old_left  > fixed_x >=  new_left and type(self.game_map.locate_cell(self.rect.center).next[next_direction]) in [Coin,Super_coin,Empty_cell,Ghost_door]:
                    self.rect.left = fixed_x
                    self.direction = self.next_moves.pop(0)
                    if next_direction == "top":
                        self.rect.centery -= old_left - new_left
                    elif next_direction == "bottom":
                        self.rect.centery += old_left - new_left

            elif self.direction == "right":
                old_right = old_rect.right
                new_right = self.rect.right
                fixed_x = old_right+cell_width-old_right%cell_width
                if old_right  < fixed_x <=  new_right and type(self.game_map.locate_cell(self.rect.center).next[next_direction]) in [Coin,Super_coin,Empty_cell,Ghost_door]:
                    self.rect.right = fixed_x
                    self.direction = self.next_moves.pop(0)
                    if next_direction == "top":
                        self.rect.centery -= new_right - old_right
                    elif next_direction == "bottom":
                        self.rect.centery += new_right - old_right

    def check_walls(self):

        colliding = pygame.sprite.spritecollide(self,self.group,False,lambda a,b :a.rect.colliderect(b.rect))
        walls = [sprite for sprite in colliding if isinstance(sprite, Wall)]
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
        ghost_door = self.game_map.ghost_door.rect
        if self.rect.colliderect(ghost_door) and self.direction == "bottom" and self.rect.bottom >= ghost_door.top:
            self.rect.bottom  = ghost_door.top
            self.direction = None

        cell_width = round(self.width) + round(self.width) % 2
        if self.rect.left > self.game_map.x_cells * cell_width:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = self.game_map.y_cells * cell_width