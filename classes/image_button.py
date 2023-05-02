from classes.image import Image

class Image_button(Image):

    def __init__(
            self, 
            name: list[str],
            winsize: list,
            scale_axis: 
            list[int], 
            loc: list[list], 
            parent_groups: list, 
            border: list[int], 
            alpha: int = 255, 
            layer: int = 0, 
            living: bool = True
        ):
        super().__init__(name, winsize, scale_axis, loc, parent_groups, border, alpha, layer, living)

        self.clicking = False
        self.hoverable = True
        self.hovering = False

    
    def update(self,new_winsize,dt,cursor):
        """Actualisation du sprite ayant lieu à chaque changement image"""

        if self.winsize != new_winsize:
            self.rescale(new_winsize)

        if self.rect.collidepoint(cursor) and self.hoverable:
            self.hovering = True
        else:
            self.hovering = False

        self.manage_frames(dt)


    def set_clicking(self,state:bool):
        """
        méthode d'écriture de l'attribut 'clicking'
        """
        
        if self.hoverable:
            self.clicking = state

    
    def set_hoverable(self,state:bool):

        self.hoverable = state


