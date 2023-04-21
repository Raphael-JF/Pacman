import pygame


class Map_generator(pygame.sprite.Sprite):

    def __init__(
        self,
        winsize:list,
        size:list,
        grid_dimensions:list,
        loc:list,
        background_clr:tuple,
        parent_groups:list,
        border:list = [-1,(0,0,0),],
        alpha:int = 255,
        living:bool = True,
        layer:int = 0
        ):
        """
        winsize = [width:int,height:int] -> taille de la fenetre pygame
        size = [width:int,height:int] -> taille de la box
        grid_dimensions = [width:int,height:int] -> nombre de cellules de la map
        loc = [[x:int,y:int],mode:str] -> coordonnées et mode de placement ('center', 'topleft', 'topright', 'bottomleft','bottomright','midtop', midright', 'midbottom','midleft')
        background_clr = [r:int,g:int,b:int,alpha:int|None] -> couleur de fond de la boîte
        parent_groups -> liste des groupes auxquels le sprite est rattaché
        border = [bd_width:int,bd_clr:tuple,bd_padding:int,border_mode:str] -> bd_width est l'épaisseur de la bordure : pour ne pas en avoir, insérer une valeur négative. bd_clr est la couleur de la bordure. bd_padding est l'espacement entre le bout de la surface et la bordure. border_mode ('inset' ou 'outset') définit si la bordure est intérieur ou extérieur à la surface (comme en html-css).
        living -> booléen indiquant si à sa création le sprite doit exister dans ses groupes ('living' car selon pygame, un sprite mort est un sprite qui n'appartient à aucun groupe)
        layer -> couche sur laquelle afficher le sprite en partant de 0. Plus layer est élevée, plus la surface sera mise en avant.
        """

        super().__init__()

        self.winsize = winsize
        self.width = size[0]
        self.height = size[1]

        self._layer = layer
        self.parent_groups = parent_groups

        self.pos = list(loc[0])
        self.placement_mode = loc[1]
        self.border_width = border[0]
        self.border_clr = border[1]

        self.alpha = alpha
        self.background_clr = list(background_clr)

        
        if len(self.background_clr) != 4:
            self.background_clr.append(255)

        if len(self.border_clr) != 4:
            self.border_clr.append(255)

        if living:
            self.liven()

        self.matrix = []
        for y in range(grid_dimensions[0]/2):
            self.matrix.append([])
            for x in range(grid_dimensions[1]):
                self.matrix[x].append('X')

[[x,x,x,x],
[x,x,x,x],
[x,x,x,x]]