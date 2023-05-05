import pygame
from classes.title import Title
from classes.transition import Transition

from assets import TIME_TICKING

class Button(Title):
    """
    Héritant de l'objet Title, Button implémente la possibilité de réagir à une action utilisateur et de changer certains de ses paramètres en fonction des états du sprite (clické, survolé...)
    """

    def __init__(
        self,
        winsize:list,
        loc:list,
        background_clr:tuple,
        font_clrs:list,
        parent_groups:list,
        size:list,
        font_size:int = 0,
        border:list = [0,(0,0,0),0,"inset"],
        text:str = "",
        font_family:str = "Arial",
        text_align:list = [0,'center'],
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
        super().__init__(
            winsize = winsize,
            loc = loc,
            background_clr = background_clr,
            size = size,
            border = border,
            font_clrs = font_clrs,
            font_size = font_size,
            text = text,
            font_family = font_family,
            text_align = text_align,
            layer = layer,
            living = living,
            parent_groups = parent_groups
        )
        self.clicking = False
        self.hovering = False
        self.hovering_changed = False
        self.clicking_changed = False
    
    
    def update(self,new_winsize,dt,cursor):
        """Actualisation du sprite ayant lieu à chaque changement image"""

        if self.winsize != new_winsize:
            self.rescale(new_winsize)
        self.manage_frames(dt)
        self.hovering_changed = False
        self.clicking_changed = False

    
    def set_clicking(self,state:bool):
        """
        méthode d'écriture de l'attribut 'clicking'
        """
        
        if state != self.clicking:
            self.clicking_changed = True
            self.clicking = state


    def set_hovering(self,state:bool):
        
        if state != self.hovering:
            self.hovering_changed = True
            self.hovering = state

