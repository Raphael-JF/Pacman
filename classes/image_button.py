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
        self.hovering = False
        self.hovering_changed = False
        self.clicking_changed = False

    
    def update(self,new_winsize,dt,cursor):
        """Actualisation du sprite ayant lieu à chaque changement image"""

        if self.winsize != new_winsize:
            self.rescale(new_winsize)  
        if self.cur_resize_frames:
            print(self.cur_resize_frames.get_list_of_values())
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

