from classes.title import Title
from classes.box import Box

class Slider(Box):
    """
    Héritant de l'objet Title, Slide implémente un widget permettant à l'utilisateur de sélectionner une valeur précise en déplaçant un curseur le long d'un segment.
    """
    def __init__(
        self,
        winsize:list,
        loc:list,
        background_clr:tuple,
        hov_background_clr:list,
        font_clrs:list,
        parent_groups:list,
        font_size:int,
        size:list,
        options_list:list[str],
        base_option:str,
        cursor_width:int,
        cursor_background_clr:list,
        hov_cursor_background_clr:list,
        hov_border:list,
        anchor_options:bool = True,
        cursor_border:list = [0,(0,0,0)],
        hov_cursor_border:list = [0,(0,0,0)],
        border:list = [0,(0,0,0),0,"inset"],
        ease_seconds:int = 0,
        ease_mode:str = "inout",
        text:str = "{}",
        font_family:str = "RopaSans-Regular.ttf",
        layer:int = 0,
        living:bool = True
    ):
        """
        ease_seconds = temps d'animation en secondes
        ease_mode = 'in','out','inout' -> mode d'animation
        hov_background_clr -> couleur en survol (hover)
        hov_border =  [bd_width:int,bd_clr:tuple,bd_padding:int] -> bordure en survol
        active_background_clr -> couleur que prend le fond du sprite quand il est cliqué (quand le clic et maintenu)
        active_border -> [bd_width:int,bd_clr:tuple,bd_padding:int], 

        Pour des informations sur d'autres attributs, se référer à la docu de Title.__init__()

        """

        x = ((size[0] - cursor_width)/(len(options_list) - 1))*options_list.index(base_option) + cursor_width/2
        if x < cursor_width / 2:
            x = cursor_width / 2
        if x > size[0] - cursor_width / 2:
            x = size[0] - cursor_width / 2

        self.text = Title(
            winsize = winsize,
            loc = [(0,0),'topleft'],
            background_clr = (0,0,0,0),
            font_clrs = font_clrs,
            font_size = font_size,
            parent_groups = [],
            size = size,
            border = [-1,(0,0,0),0,"inset"],
            text = text.format(base_option),
            font_family = font_family,
            layer = 2,
            living = True
        )

        self.cursor = Box(
            winsize = winsize,
            size = [cursor_width,size[1]],
            loc = [(x,0),'midtop'],
            background_clr = cursor_background_clr,
            parent_groups = [],
            border = cursor_border[:]+[0,"inset"],
            alpha = 255,
            living = True,
            layer = 1,
        )

        super().__init__(
            winsize = winsize,
            size = size,
            loc = loc,
            background_clr = background_clr,
            parent_groups = parent_groups,
            border = border,
            living = living,
            layer = layer
        )

        self.base_cursor_background_clr = cursor_background_clr[:]
        self.base_cursor_border_width = cursor_border[0]
        self.base_cursor_border_clr = cursor_border[1][:]

        self.hov_cursor_background_clr = hov_cursor_background_clr
        self.hov_cursor_border_width = hov_cursor_border[0]
        self.hov_cursor_border_clr = hov_cursor_border[1][:]
        
        self.base_background_clr = self.background_clr[:]
        self.base_border_width = self.border_width
        self.base_border_clr = self.border_clr
        self.base_border_padding = self.border_padding

        self.hov_background_clr = hov_background_clr
        self.hov_border_width = hov_border[0]
        self.hov_border_clr = hov_border[1]
        self.hov_border_padding = hov_border[2]

        self.anchor_options = anchor_options
        self.text_str = text
        self.ease_seconds = ease_seconds
        self.ease_mode = ease_mode
        self.clicking = False
        self.hovering = False
        self.options_list = options_list
        self.cur_option = base_option
    

    def update(self,new_winsize,dt,cursor):
        """Actualisation du sprite ayant lieu à chaque changement image"""

        if self.winsize != new_winsize:
            self.rescale(new_winsize)

        if self.clicking:
            rel_x = cursor[0] - self.rect.topleft[0]
            fractions = [i*((self.width - self.cursor.width) / (len(self.options_list)-1)) + self.cursor.width/2 for i in range(len(self.options_list))]
            if self.anchor_options:
                x = min(fractions, key=lambda a: abs(a - rel_x))
                index = fractions.index(x)
            else:
                index = fractions.index(min(fractions, key=lambda a: abs(a - rel_x)))
                x = rel_x
                if rel_x < self.cursor.width / 2:
                    x = self.cursor.width / 2
                if rel_x > self.width - self.cursor.width / 2:
                    x = self.width - self.cursor.width / 2
            if round(x) != self.cursor.pos[0]:
                self.cursor.pos[0] = x
                self.cursor.calc_rect()
                self.cur_option = self.options_list[index]
                self.text.set_text(self.text_str.format(self.cur_option))
                self.calc_image()

        self.state_changing(cursor)
        self.manage_frames(dt)
        self.cursor.manage_frames(dt)

        if self.border_clr_iter_nb != 0:
            self.calc_image()


    def calc_image(self):
        """
        Recalcul de la surface du sprite
        """
        super().calc_image()
        self.image.blit(self.cursor.image,self.cursor.rect)
        self.image.blit(self.text.image,self.text.rect)


    def rescale(self,new_winsize):
        """actualisation des valeurs en cas de changement de résolution"""
        
        super().rescale(new_winsize)
        self.cursor.rescale(new_winsize)
        self.text.rescale(new_winsize)
        self.base_cursor_border_width *= self.ratio
        self.hov_cursor_border_width *= self.ratio

        self.base_border_width *= self.ratio
        self.base_border_padding *= self.ratio
        
        self.hov_border_width *= self.ratio
        self.hov_border_padding *= self.ratio

        self.calc_image()

    
    def state_changing(self,cursor):

        if self.rect.collidepoint(cursor) or self.clicking:
            new_state = True
        elif self.clicking:
            new_state = True
        else:
            new_state = False

        if self.hovering != new_state:
            self.hovering = new_state
            if not self.hovering:
                self.instant_change_background_clr([self.background_clr,self.base_background_clr],[self.ease_seconds],[self.ease_mode])
                self.instant_change_border_width([self.border_width,self.base_border_width],[self.ease_seconds],[self.ease_mode])
                self.instant_change_border_clr([self.border_clr,self.base_border_clr],[self.ease_seconds],[self.ease_mode])
                self.instant_change_border_padding([self.border_padding,self.base_border_padding],[self.ease_seconds],[self.ease_mode])
                self.cursor.instant_change_background_clr([self.cursor.background_clr,self.base_cursor_background_clr],[self.ease_seconds],[self.ease_mode])
                self.cursor.instant_change_border_width([self.cursor.border_width,self.base_cursor_border_width],[self.ease_seconds],[self.ease_mode])
                self.cursor.instant_change_border_clr([self.cursor.border_clr,self.base_cursor_border_clr],[self.ease_seconds],[self.ease_mode])
            else:
                self.instant_change_background_clr([self.background_clr,self.hov_background_clr],[self.ease_seconds],[self.ease_mode])
                self.instant_change_border_width([self.border_width,self.hov_border_width],[self.ease_seconds],[self.ease_mode])
                self.instant_change_border_clr([self.border_clr,self.hov_border_clr],[self.ease_seconds],[self.ease_mode])
                self.instant_change_border_padding([self.border_padding,self.hov_border_padding],[self.ease_seconds],[self.ease_mode])
                self.cursor.instant_change_background_clr([self.cursor.background_clr,self.hov_cursor_background_clr],[self.ease_seconds],[self.ease_mode])
                self.cursor.instant_change_border_width([self.cursor.border_width,self.hov_cursor_border_width],[self.ease_seconds],[self.ease_mode])
                self.cursor.instant_change_border_clr([self.cursor.border_clr,self.hov_cursor_border_clr],[self.ease_seconds],[self.ease_mode])

    
    def set_clicking(self,state:bool):
        """
        méthode d'écriture de l'attribut 'clicking'
        """

        self.clicking = state

    
    def set_option(self,option:str):
        """
        définit comme option actuelle l'option renseignée.
        """
        x = ((self.width - self.cursor.width)/(len(self.options_list) - 1))*self.options_list.index(option) + self.cursor.width/2
        if x < self.cursor.width / 2:
            x = self.cursor.width / 2
        if x > self.width - self.cursor.width / 2:
            x = self.width - self.cursor.width / 2
        self.cursor.pos[0] = x
        self.cursor.calc_rect()
        self.cur_option = option
        self.text.set_text(self.text_str.format(self.cur_option))
        self.calc_image()

