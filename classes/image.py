import math,pygame,os,assets
from classes.transition import Transition


def rescale_values(values,winsize,cur_value):
    if values != cur_value:
        if type(values) in (list,tuple):
            return [rescale_values(i,winsize,cur_value) for i in values]
        return values * winsize[0] / assets.BASE_SIZE[0]
    else:
        return values


class Image(pygame.sprite.Sprite):
    def __init__(
        self, 
        name: list[str], 
        winsize: list, 
        scale_axis: list[int,str], 
        loc: list[list,str], 
        parent_groups: list,
        border:list[int,list,int,str],
        alpha:int = 255,
        layer: int = 0, 
        living: bool = True,
    ):
        """
        winsize = [width:int,height:int] -> taille fenetre pygame
        name = str -> chemin absolu vers l'image en partant du dossier 'images'. Aucune extension n'est concaténée.
        scale_axis = [value:int,x_or_y:str] -> taille voulue pour l'axe x ou y
        loc = [[x:int,y:int],mode:str] -> coordonnées et mode de placement ('center', 'topleft', 'topright', 'bottomleft','bottomright','midtop', midright', 'midbottom','midleft')
        degrees -> angle d'affichage de l'image
        border = [bd_width:int,bd_clr:tuple] -> bd_width est l'épaisseur de la bordure : pour ne pas en avoir, insérer une valeur négative. bd_clr est la couleur de la bordure. 
        layer -> couche sur laquelle afficher le sprite en partant de 1. Plus layer est élevée, plus la surface sera mise en avant.

        """

        super().__init__()
        
        self.winsize = winsize
        self._layer = layer
        self.pos = loc[0]
        self.placement_mode = loc[1]
        self.border_position = border[3]
        self.parent_groups = parent_groups
        self.contenu = pygame.image.load(os.path.join(os.getcwd(),'images',*name))

        if scale_axis[1] == "x":
            self.height = (scale_axis[0]*self.contenu.get_height()) / self.contenu.get_width()
            self.width = scale_axis[0]
            
        elif scale_axis[1] == "y":
            self.width = (scale_axis[0]*self.contenu.get_width()) / self.contenu.get_height()
            self.height = scale_axis[0]

        else:
            raise ValueError("scale_axis[1] doit être 'x' ou 'y'")


        self.border_width = border[0]
        self.cur_border_width_frames:Transition = None
        self.inf_border_width_frames:Transition = None
        self.border_width_iter_nb = 0
        self.border_width_frames_list:list[tuple[Transition,int]] = []

        self.border_clr = list(border[1])
        self.cur_border_clr_frames:Transition = None
        self.inf_border_clr_frames:Transition = None
        self.border_clr_iter_nb = 0
        self.border_clr_frames_list:list[tuple[Transition,int]] = []

        self.border_padding = border[2]
        self.cur_border_padding_frames:Transition = None
        self.inf_border_padding_frames:Transition = None
        self.border_padding_iter_nb = 0
        self.border_padding_frames_list:list[tuple[Transition,int]] = []

        self.cur_translate_frames:Transition = None
        self.translate_iter_nb = 0
        self.translate_frames_list:list[tuple[Transition,int]] = []
        self.inf_translate_frames:Transition = None

        self.resize_ratio = 1
        self.cur_resize_frames:Transition = None
        self.resize_iter_nb = 0
        self.resize_frames_list:list[tuple[Transition,int]] = []
        self.inf_resize_frames:Transition = None

        self.degrees = 0
        self.cur_degrees_frames:Transition = None
        self.degrees_iter_nb = 0
        self.degrees_frames_list:list[tuple[Transition,int]] = []
        self.inf_degrees_frames:Transition = None
        
        self.alpha = alpha
        self.cur_alpha_frames:Transition = None
        self.alpha_iter_nb = 0
        self.alpha_frames_list:list[tuple[Transition,int]] = []
        self.inf_alpha_frames:Transition = None

        if len(self.border_clr) != 4:
            self.border_clr.append(255)

        self.calc_image()
        self.calc_rect()

        if living:
            self.liven()


    def liven(self):

        for group in self.parent_groups:
            group.add(self)
                      

    def update(self,new_winsize,dt,cursor):
        """Actualisation du sprite ayant lieu à chaque changement image"""

        if self.winsize != new_winsize:
            self.rescale(new_winsize = new_winsize)

        self.manage_frames(dt)

    
    def calc_image(self):
        """
        Recalcul de la surface du sprite (sa taille).
        """

        width = round(self.width) + round(self.width) % 2
        height = round(self.height) + round(self.height) % 2
        border_padding2 = round(self.border_padding*2) + round(self.border_padding*2) % 2
        border_width2 = round(self.border_width*2) + round(self.border_width*2) % 2

        img_surf = pygame.transform.smoothscale(self.contenu,(round(self.width*self.resize_ratio),round(self.height*self.resize_ratio)))

        if self.border_position == "inset":
            self.image = pygame.Surface([
                round(width*self.resize_ratio),
                round(height*self.resize_ratio)
                ],pygame.SRCALPHA)
            self.image.blit(img_surf,img_surf.get_rect(center = [round(width*self.resize_ratio/2),round(height*self.resize_ratio/2)]))

            border_rect = pygame.Rect(
                0,
                0, 
                round((width - border_padding2)*self.resize_ratio), 
                round((height - border_padding2)*self.resize_ratio))

            border_rect.center = self.image.get_rect().center

            pygame.draw.rect(
            self.image,
            self.border_clr,
            border_rect,
            round(self.border_width*self.resize_ratio)
            )

        elif self.border_position == "outset":
            self.image = pygame.Surface([
                round((width + border_width2 + border_padding2)*self.resize_ratio),
                round((height + border_width2 + border_padding2)*self.resize_ratio)],pygame.SRCALPHA)
            self.image.blit(img_surf,img_surf.get_rect(center = [round((height + border_width2 + border_padding2)*self.resize_ratio/2),round((height + border_width2 + border_padding2)*self.resize_ratio)]))



            border_rect = pygame.Rect(
                0,
                0, 
                round((width + round(self.border_width*2))*self.resize_ratio), 
                round((height + round(self.border_width*2))*self.resize_ratio))
            border_rect.center = self.image.get_rect().center
            pygame.draw.rect(
            self.image,
            self.border_clr,
            border_rect,
            round(self.border_width*self.resize_ratio)
            )

        else:
            raise ValueError ("border_position must be 'inset' or 'outset'")
        
        if self.degrees != 0:
            self.image = pygame.transform.rotate(self.image,round(self.degrees,2))

        if self.alpha != 255:
            self.image.set_alpha(self.alpha)

    
    def calc_rect(self):
        """
        Recalcul du rectangle du sprite (ses coordonnées).
        """

        pos = [round(i) for i in self.pos]
        if self.placement_mode == "topleft":
            self.rect = self.image.get_rect(topleft=pos)
        elif self.placement_mode == "topright":
            self.rect = self.image.get_rect(topright=pos)
        elif self.placement_mode == "bottomleft":
            self.rect = self.image.get_rect(bottomleft=pos)
        elif self.placement_mode == "bottomright":
            self.rect = self.image.get_rect(bottomright=pos)
        elif self.placement_mode == "midtop":
            self.rect = self.image.get_rect(midtop=pos)
        elif self.placement_mode == "midleft":
            self.rect = self.image.get_rect(midleft=pos)
        elif self.placement_mode == "midbottom":
            self.rect = self.image.get_rect(midbottom=pos)
        elif self.placement_mode == "midright":
            self.rect = self.image.get_rect(midright=pos)
        elif self.placement_mode == "center":
            self.rect = self.image.get_rect(center=pos)


    def change_name(self,new_name):
        
        self.contenu = pygame.image.load(os.path.join(os.getcwd(),'images',*new_name))


    def manage_frames(self,dt):

        calc_image1,calc_both1,calc_both2,calc_both3,calc_both4,calc_rect1,calc_rect2 = [False]*7
        
        if self.border_width_iter_nb > 0:
            self.border_width, calc_both1, finish = self.cur_border_width_frames.change_index(dt,self.border_width)
            if finish:
                if self.border_width_iter_nb == math.inf and len(self.border_width_frames_list) > 0:
                    self.cur_border_width_frames, self.border_width_iter_nb = self.border_width_frames_list.pop(0)
                self.border_width_iter_nb -= 1
                if self.border_width_iter_nb > 0:
                    self.cur_border_width_frames.reset_index()
                elif len(self.border_width_frames_list) > 0:
                    self.cur_border_width_frames, self.border_width_iter_nb = self.border_width_frames_list.pop(0)
                elif self.inf_border_width_frames:
                        self.cur_border_width_frames = self.inf_border_width_frames
                        self.border_width_iter_nb = math.inf
        
        if self.border_clr_iter_nb > 0:
            self.border_clr, calc_rect1, finish = self.cur_border_clr_frames.change_index(dt,self.border_clr)
            if finish:
                if self.border_clr_iter_nb == math.inf and len(self.border_clr_frames_list) > 0:
                    self.cur_border_clr_frames, self.border_clr_iter_nb = self.border_clr_frames_list.pop(0)
                self.border_clr_iter_nb -= 1
                if self.border_clr_iter_nb > 0:
                    self.cur_border_clr_frames.reset_index()
                elif len(self.border_clr_frames_list) > 0:
                    self.cur_border_clr_frames, self.border_clr_iter_nb = self.border_clr_frames_list.pop(0)
                elif self.inf_border_clr_frames:
                        self.cur_border_clr_frames = self.inf_border_clr_frames
                        self.border_clr_iter_nb = math.inf
        
        if self.border_padding_iter_nb > 0:
            self.border_padding, calc_both2, finish = self.cur_border_padding_frames.change_index(dt,self.border_padding)
            if finish:
                if self.border_padding_iter_nb == math.inf and len(self.border_padding_frames_list) > 0:
                    self.cur_border_padding_frames, self.border_padding_iter_nb = self.border_padding_frames_list.pop(0)
                self.border_padding_iter_nb -= 1
                if self.border_padding_iter_nb > 0:
                    self.cur_border_padding_frames.reset_index()
                elif len(self.border_padding_frames_list) > 0:
                    self.cur_border_padding_frames, self.border_padding_iter_nb = self.border_padding_frames_list.pop(0)
                elif self.inf_border_padding_frames:
                        self.cur_border_padding_frames = self.inf_border_padding_frames
                        self.border_padding_iter_nb = math.inf

        if self.translate_iter_nb > 0:
            self.pos, calc_rect2, finish = self.cur_translate_frames.change_index(dt,self.pos)
            if finish:
                if self.translate_iter_nb == math.inf and len(self.translate_frames_list) > 0:
                    self.cur_translate_frames, self.translate_iter_nb = self.translate_frames_list.pop(0)
                self.translate_iter_nb -= 1
                if self.translate_iter_nb > 0:
                    self.cur_translate_frames.reset_index()
                elif len(self.translate_frames_list) > 0:
                    self.cur_translate_frames, self.translate_iter_nb = self.translate_frames_list.pop(0)
                elif self.inf_translate_frames:
                        self.cur_translate_frames = self.inf_translate_frames
                        self.translate_iter_nb = math.inf
        
        if self.resize_iter_nb > 0:
            self.resize_ratio, calc_both3, finish = self.cur_resize_frames.change_index(dt,self.resize_ratio)
            if finish:
                if self.resize_iter_nb == math.inf and len(self.resize_frames_list) > 0:
                    self.cur_resize_frames, self.resize_iter_nb = self.resize_frames_list.pop(0)
                self.resize_iter_nb -= 1
                if self.resize_iter_nb > 0:
                    self.cur_resize_frames.reset_index()
                elif len(self.resize_frames_list) > 0:
                    self.cur_resize_frames, self.resize_iter_nb = self.resize_frames_list.pop(0)
                elif self.inf_resize_frames:
                        self.cur_resize_frames = self.inf_resize_frames
                        self.resize_iter_nb = math.inf

        if self.degrees_iter_nb > 0:
            self.degrees, calc_both4, finish = self.cur_degrees_frames.change_index(dt,self.degrees)
            if finish:
                if self.degrees_iter_nb == math.inf and len(self.degrees_frames_list) > 0:
                    self.cur_degrees_frames, self.degrees_iter_nb = self.degrees_frames_list.pop(0)
                self.degrees_iter_nb -= 1
                if self.degrees_iter_nb > 0:
                    self.cur_degrees_frames.reset_index()
                elif len(self.degrees_frames_list) > 0:
                    self.cur_degrees_frames, self.degrees_iter_nb = self.degrees_frames_list.pop(0)
                elif self.inf_degrees_frames:
                        self.cur_degrees_frames = self.inf_degrees_frames
                        self.degrees_iter_nb = math.inf
        
        if self.alpha_iter_nb > 0:
            self.alpha, calc_image1, finish = self.cur_alpha_frames.change_index(dt,self.alpha)
            if finish:
                if self.alpha_iter_nb == math.inf and len(self.alpha_frames_list) > 0:
                    self.cur_alpha_frames, self.alpha_iter_nb = self.alpha_frames_list.pop(0)
                self.alpha_iter_nb -= 1
                if self.alpha_iter_nb > 0:
                    self.cur_alpha_frames.reset_index()
                elif len(self.alpha_frames_list) > 0:
                    self.cur_alpha_frames, self.alpha_iter_nb = self.alpha_frames_list.pop(0)
                elif self.inf_alpha_frames:
                        self.cur_alpha_frames = self.inf_alpha_frames
                        self.alpha_iter_nb = math.inf

        if round(self.alpha) == 0 and self.alpha_iter_nb == 0:
            self.kill()

        if calc_both1 or calc_both2 or calc_both3 or calc_both4:
            self.calc_image()
            self.calc_rect()

        else:
            if calc_image1 or calc_image1:
                self.calc_image()
            if calc_rect1 or calc_rect2:
                self.calc_rect()  


    def rescale(self,new_winsize):
        """actualisation des valeurs en cas de changement de résolution"""

        old_winsize = self.winsize[:]
        self.winsize = new_winsize

        self.ratio = self.winsize[0] / old_winsize[0]

        self.width *= self.ratio
        self.height *= self.ratio
        self.border_width *= self.ratio
        self.border_padding *= self.ratio
        self.pos = [i*self.ratio for i in self.pos]

        if round(self.width) % 2 != 1:
            self.width += 1

        if round(self.height) %2 != 1:
            self.height += 1

        for transition in [i[0] for i in self.border_width_frames_list] + [self.cur_border_width_frames,self.inf_border_width_frames]:
            if transition is not None:
                transition.rescale_step_values(self.ratio)

        for transition in [i[0] for i in self.border_padding_frames_list] + [self.cur_border_padding_frames,self.inf_border_padding_frames]:
            if transition is not None:
                transition.rescale_step_values(self.ratio)

        for transition in [i[0] for i in self.translate_frames_list] + [self.cur_translate_frames,self.inf_translate_frames]:
            if transition is not None:
                transition.rescale_step_values(self.ratio)
        
        self.calc_image()
        self.calc_rect()


    def change_border_width(self,values:list,ease_seconds:list,ease_modes:list,iter_nb:int = math.inf):
        
        values = rescale_values(values,self.winsize,self.border_width)
        if iter_nb == math.inf:
            self.inf_border_width_frames = Transition(values,ease_seconds,ease_modes)
            if self.cur_border_width_frames is None or self.border_width_iter_nb == 0:
                self.cur_border_width_frames = self.inf_border_width_frames
                self.border_width_iter_nb = math.inf
        else:
            if self.cur_border_width_frames is None or self.border_width_iter_nb == 0:
                self.cur_border_width_frames = Transition(values,ease_seconds,ease_modes)
                self.border_width_iter_nb = iter_nb
            elif self.border_width_iter_nb == math.inf:
                self.cur_border_width_frames = Transition(values,ease_seconds,ease_modes)
                self.border_width_iter_nb = iter_nb
            else:
                self.border_width_frames_list.append((Transition(values,ease_seconds,ease_modes),iter_nb))


    def instant_change_border_width(self,values:list,ease_seconds:list,ease_modes:list):

        values = rescale_values(values,self.winsize,self.border_width)
        self.cur_border_width_frames = Transition(values,ease_seconds,ease_modes)
        self.border_width_iter_nb = 1


    def change_border_clr(self,values:list,ease_seconds:list,ease_modes:list,iter_nb:int = math.inf):
        
        if iter_nb == math.inf:
            self.inf_border_clr_frames = Transition(values,ease_seconds,ease_modes)
            if self.cur_border_clr_frames is None or self.border_clr_iter_nb == 0:
                self.cur_border_clr_frames = self.inf_border_clr_frames
                self.border_clr_iter_nb = math.inf
        else:
            if self.cur_border_clr_frames is None or self.border_clr_iter_nb == 0:
                self.cur_border_clr_frames = Transition(values,ease_seconds,ease_modes)
                self.border_clr_iter_nb = iter_nb
            elif self.border_clr_iter_nb == math.inf:
                self.cur_border_clr_frames = Transition(values,ease_seconds,ease_modes)
                self.border_clr_iter_nb = iter_nb
            else:
                self.border_clr_frames_list.append((Transition(values,ease_seconds,ease_modes),iter_nb))


    def instant_change_border_clr(self,values:list,ease_seconds:list,ease_modes:list):

        self.cur_border_clr_frames = Transition(values,ease_seconds,ease_modes)
        self.border_clr_iter_nb = 1

        
    def change_border_padding(self,values:list,ease_seconds:list,ease_modes:list,iter_nb:int = math.inf):
        
        values = rescale_values(values,self.winsize,self.border_padding)
        if iter_nb == math.inf:
            self.inf_border_padding_frames = Transition(values,ease_seconds,ease_modes)
            if self.cur_border_padding_frames is None or self.border_padding_iter_nb == 0:
                self.cur_border_padding_frames = self.inf_border_padding_frames
                self.border_padding_iter_nb = math.inf
        else:
            if self.cur_border_padding_frames is None or self.border_padding_iter_nb == 0:
                self.cur_border_padding_frames = Transition(values,ease_seconds,ease_modes)
                self.border_padding_iter_nb = iter_nb
            elif self.border_padding_iter_nb == math.inf:
                self.cur_border_padding_frames = Transition(values,ease_seconds,ease_modes)
                self.border_padding_iter_nb = iter_nb
            else:
                self.border_padding_frames_list.append((Transition(values,ease_seconds,ease_modes),iter_nb))

    def instant_change_border_padding(self,values:list,ease_seconds:list,ease_modes:list):

        values = rescale_values(values,self.winsize,self.border_padding)
        self.cur_border_padding_frames = Transition(values,ease_seconds,ease_modes)
        self.border_padding_iter_nb = 1


    def translate(self,values:list,ease_seconds:list,ease_modes:list,iter_nb:int = math.inf):
        
        values = rescale_values(values,self.winsize,self.pos)
        if iter_nb == math.inf:
            self.inf_translate_frames = Transition(values,ease_seconds,ease_modes)
            if self.cur_translate_frames is None or self.translate_iter_nb == 0:
                self.cur_translate_frames = self.inf_translate_frames
                self.translate_iter_nb = math.inf
        else:
            if self.cur_translate_frames is None or self.translate_iter_nb == 0:
                self.cur_translate_frames = Transition(values,ease_seconds,ease_modes)
                self.translate_iter_nb = iter_nb
            elif self.translate_iter_nb == math.inf:
                self.cur_translate_frames = Transition(values,ease_seconds,ease_modes)
                self.translate_iter_nb = iter_nb
            else:
                self.translate_frames_list.append((Transition(values,ease_seconds,ease_modes),iter_nb))
    

    def instant_translate(self,values:list,ease_seconds:list,ease_modes:list):

        values = rescale_values(values,self.winsize,self.pos)
        self.cur_translate_frames = Transition(values,ease_seconds,ease_modes)
        self.translate_iter_nb = 1


    def resize(self,values:list,ease_seconds:list,ease_modes:list,iter_nb:int = math.inf):
        
        if iter_nb == math.inf:
            self.inf_resize_frames = Transition(values,ease_seconds,ease_modes)
            if self.cur_resize_frames is None or self.resize_iter_nb == 0:
                self.cur_resize_frames = self.inf_resize_frames
                self.resize_iter_nb = math.inf
        else:
            if self.cur_resize_frames is None or self.resize_iter_nb == 0:
                self.cur_resize_frames = Transition(values,ease_seconds,ease_modes)
                self.resize_iter_nb = iter_nb
            elif self.resize_iter_nb == math.inf:
                self.cur_resize_frames = Transition(values,ease_seconds,ease_modes)
                self.resize_iter_nb = iter_nb
            else:
                self.resize_frames_list.append((Transition(values,ease_seconds,ease_modes),iter_nb))
    
    
    def instant_resize(self,values:list,ease_seconds:list,ease_modes:list):

        self.cur_resize_frames = Transition(values,ease_seconds,ease_modes)
        self.resize_iter_nb = 1

    
    def rotate(self,values:list,ease_seconds:list,ease_modes:list,iter_nb:int = math.inf):
        
        if iter_nb == math.inf:
            self.inf_degrees_frames = Transition(values,ease_seconds,ease_modes)
            if self.cur_degrees_frames is None or self.degrees_iter_nb == 0:
                self.cur_degrees_frames = self.inf_degrees_frames
                self.degrees_iter_nb = math.inf
        else:
            if self.cur_degrees_frames is None or self.degrees_iter_nb == 0:
                self.cur_degrees_frames = Transition(values,ease_seconds,ease_modes)
                self.degrees_iter_nb = iter_nb
            elif self.degrees_iter_nb == math.inf:
                self.cur_degrees_frames = Transition(values,ease_seconds,ease_modes)
                self.degrees_iter_nb = iter_nb
            else:
                self.degrees_frames_list.append((Transition(values,ease_seconds,ease_modes),iter_nb))
    
    
    def instant_rotate(self,values:list,ease_seconds:list,ease_modes:list):

        self.cur_degrees_frames = Transition(values,ease_seconds,ease_modes)
        self.degrees_iter_nb = 1


    def change_alpha(self,values:list,ease_seconds:list,ease_modes:list,iter_nb:int = math.inf):
    
        if not self.alive():
            self.liven()

        if iter_nb == math.inf:
            self.inf_alpha_frames = Transition(values,ease_seconds,ease_modes)
            if self.cur_alpha_frames is None or self.alpha_iter_nb == 0:
                self.cur_alpha_frames = self.inf_alpha_frames
                self.alpha_iter_nb = math.inf
        else:
            if self.cur_alpha_frames is None or self.alpha_iter_nb == 0:
                self.cur_alpha_frames = Transition(values,ease_seconds,ease_modes)
                self.alpha_iter_nb = iter_nb
            elif self.alpha_iter_nb == math.inf:
                self.cur_alpha_frames = Transition(values,ease_seconds,ease_modes)
                self.alpha_iter_nb = iter_nb
            else:
                self.alpha_frames_list.append((Transition(values,ease_seconds,ease_modes),iter_nb))

    
    def instant_change_alpha(self,values:list,ease_seconds:list,ease_modes:list):

        if not self.alive():
            self.liven()
        self.cur_alpha_frames = Transition(values,ease_seconds,ease_modes)
        self.alpha_iter_nb = 1