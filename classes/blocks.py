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
        self.state = "idle"
        self.sprite_sheets = []
        self.anim_timer = Timer(assets.PACMAN_SPRITES_DELAY,self.animate)
        self.animate()

    def update(self,dt):


        self.anim_timer.pass_time(dt)

        if self.direction is not None:
            old_pacman_rect = self.rect
            self.rect = self.get_next_rect(dt)
            self.path(old_pacman_rect)
            self.check_walls()


    def animate(self):
        
        self.anim_timer = Timer(assets.PACMAN_SPRITES_DELAY,self.animate)

        if self.state == "idle":
            return
        elif self.state == "moving":
            if len(self.sprite_sheets) == 0:
                self.sprite_sheets = assets.PACMAN_MOVING_SPRITES[:]
            
        elif self.state == "dying":
            if len(self.sprite_sheets) == 0:
                self.sprite_sheets = assets.PACMAN_DYING_SPRITES[:]
            elif len(self.sprite_sheets) == 1:
                self.game_map.finished = True
                self.game_map.pacman.kill()

        self.set_name(self.sprite_sheets.pop(0))
            
        


    def set_direction(self,new_dir):

        if self.state == "dying":
            return
        
        if self.direction != new_dir:
            self.set_state("moving")
            self.direction = new_dir
            if self.direction == "top":
                self.degrees = 90
            elif self.direction == "left":
                self.degrees = 180
            elif self.direction == "bottom":
                self.degrees = 270
            elif self.direction == "right":
                self.degrees = 0
            else:
                self.set_state("idle")
            self.calc_image()


    def set_state(self,state:str):
    
        if state != self.state:
            self.state = state
            self.sprite_sheets = []
            if state == "dying":
                self.direction = None
                self.next_direction = None


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
            self.set_state("idle")
            self.direction = None
            self.next_direction = None

        if self.rect.left > self.game_map.x_cells * self.width and self.direction == "right":
            self.rect.right = 0
        elif self.rect.right < 0 and self.direction == "left":
            self.rect.left = self.game_map.y_cells * self.width
            























class Ghost(Image):
    """
    `self.state` possibles:
    - 'wandering'
    - 'imprisoned'
    - 'escaping'
    - 'chasing'
    - 'dead'

    `self.anim_state` possibles:
    - 'base'
    - 'esc_white'
    - 'esc_blue'
    - 'dead'
    """

    def __init__(self,winsize,color,speed,topleft,width,game_map,group):

        super().__init__(
            name = ["textures","ghost",color,"right","0.png"],
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
        self.speed_multiplier = 1
        self.direction = None
        self.next_moves = []
        self.group = group
        self.state = "imprisoned"
        self.state_timer:Timer = None
        self.anim_state = "base"
        self.sprite_sheets = []
        self.anim_timer = Timer(assets.GHOST_SPRITES_DELAY,self.animate)
        self.animate()

    def animate(self):

    #         - 'base'
    # - 'esc_white'
    # - 'esc_blue'
    # - 'dead'
        self.anim_timer = Timer(assets.GHOST_SPRITES_DELAY,self.animate)
        name = self.name[:]

        if self.anim_state == "base":
            if name[-1] == "0.png":
                self.set_name(["textures","ghost",self.color,self.direction or "right","1.png"])
            else:
                self.set_name(["textures","ghost",self.color,self.direction or "right","0.png"])
        
        elif self.anim_state == "esc_blue":
            if name[-1] == "0.png":
                self.set_name(["textures","ghost","other","esc_blue","1.png"])
            else:
                self.set_name(["textures","ghost","other","esc_blue","0.png"])
        
        elif self.anim_state == "esc_white":
            if name[-1] == "0.png":
                self.set_name(["textures","ghost","other","esc_white","1.png"])
            else:
                self.set_name(["textures","ghost","other","esc_white","0.png"])



    def update(self,dt):

        self.anim_timer.pass_time(dt)

        if self.state_timer:
            self.state_timer.pass_time(dt)
        
        if self.state == "imprisoned":
            if len(self.next_moves) == 0:
                self.next_moves = ["top","bottom"]
            if self.direction is None:
                self.set_direction(self.next_moves.pop(0))
                
        elif self.state == "wandering":
            if len(self.next_moves) == 0:
                self.next_moves = ["left","right","bottom","top"]
                random.shuffle(self.next_moves)
                self.next_moves.pop(0)
            if self.direction is None:
                self.set_direction(self.next_moves.pop(0))

        elif self.state == "chasing":
            if len(self.next_moves) == 0:
                self.next_moves = self.game_map.get_moves(self.game_map.graph.dijkstra(self.next_fixed_pos(),self.game_map.pacman.next_fixed_pos()))
            if self.direction is None:
                try:
                    self.set_direction(self.next_moves.pop(0))
                except:
                    self.set_direction(random.choice(self.available_dir()))
        
        elif self.state == "escaping":
            if len(self.next_moves) == 0:
                self.next_moves = self.game_map.get_moves(self.game_map.graph.dijkstra(self.next_fixed_pos(),self.farest_from_pacman()))
            if self.direction is None:
                try:
                    self.set_direction(self.next_moves.pop(0))
                except:
                    self.set_direction(random.choice(self.available_dir()))

        elif self.state == "dead":
             if self.direction is None:
                try:
                    self.set_direction(self.next_moves.pop(0))
                except:
                    self.set_state("wandering")


        if self.direction is not None:
            old_rect = self.rect
            self.rect = self.get_next_rect(dt)
            self.path(old_rect)
            self.check_walls()

    def farest_from_pacman(self):

        pos = self.game_map.locate_pos(self.game_map.pacman.rect.center)
        if pos[1] <= self.game_map.y_cells//2:
            if pos[0] <= self.game_map.x_cells//2:
                res = self.game_map.farest_cell("bottomright",[Empty_cell,Coin,Super_coin]).rect 
            else:
                res = self.game_map.farest_cell("bottomleft",[Empty_cell,Coin,Super_coin]).rect 
        else:
            if pos[0] <= self.game_map.x_cells//2:
                res = self.game_map.farest_cell("topright",[Empty_cell,Coin,Super_coin]).rect 
            else:
                res = self.game_map.farest_cell("topleft",[Empty_cell,Coin,Super_coin]).rect 
        return self.game_map.locate_pos(res.center)


    def get_next_rect(self,dt):

        offset = [0,0]
        if self.direction is not None:
            match self.direction:
                case "top":
                    offset[1] -= self.speed*self.width*dt*self.speed_multiplier
                case "bottom":
                    offset[1] += self.speed*self.width*dt*self.speed_multiplier
                case "left":
                    offset[0] -= self.speed*self.width*dt*self.speed_multiplier
                case "right":
                    offset[0] += self.speed*self.width*dt*self.speed_multiplier
        return self.rect.move(offset)
        

    def available_dir(self):
        
        cell = self.game_map.cells[self.next_fixed_pos()[1]][self.next_fixed_pos()[0]]
        res = []
        for dir,c in cell.next.items():
            if type(c) in [Empty_cell,Coin,Super_coin]:
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
        

    def set_direction(self,dir):

        if self.direction == dir:
            return
        elif dir == "top":
            pass
        elif dir == "bottom":
            pass
        elif dir == "left":
            pass
        elif dir == "right":
            pass
        elif dir == None:
            self.direction = dir
            return
        
        self.direction = dir
        if self.anim_state == "base":
            self.set_name(["textures","ghost",self.color,self.direction,"0.png"])
        elif self.anim_state == "dead":
            self.set_name(["textures","ghost","other","dead",self.direction+".png"])


    def set_esc_blue(self,left_time):
        if left_time > assets.GHOST_BLINK_DELAY:
            self.state_timer = Timer(assets.GHOST_BLINK_DELAY,self.set_esc_white,left_time - assets.GHOST_BLINK_DELAY)
        else:
            self.state_timer = Timer(left_time,self.set_state,"wandering")
        self.anim_state = "esc_blue"
        self.set_name(["textures","ghost","other","esc_blue","0.png"])
    

    def set_esc_white(self,left_time):
        if left_time > assets.GHOST_BLINK_DELAY:
            self.state_timer = Timer(assets.GHOST_BLINK_DELAY,self.set_esc_blue,left_time - assets.GHOST_BLINK_DELAY)
        else:
            self.state_timer = Timer(left_time,self.set_state,"wandering")
        self.anim_state = "esc_white"
        self.set_name(["textures","ghost","other","esc_white","0.png"])


    def set_state(self,state):
        
        if state == self.state:
            return
        
        elif state == "chasing":
            self.anim_state = "base"
            self.set_name(["textures","ghost",self.color,self.direction or "right","0.png"])
            self.speed_multiplier = 1
            self.next_moves = []

        elif state == "wandering":
            self.anim_state = "base"
            self.set_name(["textures","ghost",self.color,self.direction or "right","0.png"])
            self.speed_multiplier = 1
            self.next_moves = []

        elif state == "escaping":
            self.speed_multiplier = 0.625
            self.next_moves = []
            self.set_direction(assets.opposite_side(self.direction))
            self.anim_state = "esc_blue"
            self.set_name(["textures","ghost","other","esc_blue","0.png"])
        
        elif state == "imprisoned":
            self.speed_multiplier = 1
            self.next_moves = []

        elif state == "dead":
            self.speed_multiplier = 2
            x,y = self.game_map.x_cells//2, self.game_map.y_cells//2
            loc = [[x-1,y-1],[x+1,y-1],[x-1,y],[x+1,y]]
            self.next_moves = self.game_map.get_moves(self.game_map.graph.dijkstra(self.next_fixed_pos(),random.choice(loc)))
            if self.direction is None:
                self.set_direction(self.next_moves.pop(0))
            self.anim_state = "dead"
            self.state_timer = None
            self.set_name(["textures","ghost","other","dead",(self.direction or "right")+".png"])

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
                    self.set_direction(self.next_moves.pop(0))
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
                    self.set_direction(self.next_moves.pop(0))
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
                    self.set_direction(self.next_moves.pop(0))
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
                    self.set_direction(self.next_moves.pop(0))
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
            self.set_direction(None)
        ghost_door = self.game_map.ghost_door.rect
        if self.rect.colliderect(ghost_door) and self.direction == "bottom" and self.rect.bottom >= ghost_door.top and not self.state == "dead":
            self.rect.bottom  = ghost_door.top
            self.set_direction(None)

        if self.rect.left > self.game_map.x_cells * self.width and self.direction == "right":
            self.rect.right = 0
        elif self.rect.right < 0 and self.direction == "left":
            self.rect.left = self.game_map.y_cells * self.width