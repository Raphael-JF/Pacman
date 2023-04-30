import assets,pygame
from classes.box import Box
from classes.image import Image

class Game_map_editor(Box):

    def __init__(
            self,
            winsize:list,
            dimensions:list[int],
            start_size:list[int],
            pos:list[int],
            background_clr:list[int],
            parent_groups:list,
            border:list,
            living:bool,
            layer:int,


    ):
        self.x_tiles, self.y_tiles = dimensions
        if self.x_tiles % 2 == 0:
            self.x_tiles += 1
        if self.y_tiles % 2 == 1:
            self.y_tiles += 1
        self.tile_width = min(start_size[0]/dimensions[0], start_size[1]/dimensions[1])

        super().__init__(winsize, [self.x_tiles * self.tile_width, self.y_tiles * self.tile_width], [pos,'center'], background_clr, parent_groups, border[:]+["outset"], 255, living, layer)

        self.tiles:list[list[Image]] = []
        self.matrix:list[list[str]] = []
        for y in range(self.y_tiles):
            temp_tiles:list[Image] = []
            temp_matrix:list[str] = []
            for x in range(self.x_tiles):
                temp_tiles.append(Image(
                    name = ["empty_cell.png"],
                    winsize = self.winsize,
                    scale_axis = ('x',self.tile_width),
                    loc = [[(x+0.5)*self.tile_width,(y+0.5)*self.tile_width],'center'],
                    parent_groups = [],
                    border = [-1,(240,240,240,0,"inset")]
                ))
                temp_matrix.append("□")
            self.tiles.append(temp_tiles)
            self.matrix.append(temp_matrix)

        for x in range(self.x_tiles):
            self.matrix[0][x] = "X"
            self.matrix[-1][x] = "X"
            self.tiles[0][x].change_name(["wall.png"])
            self.tiles[-1][x].change_name(["wall.png"])
        
        for y in range(self.y_tiles):
            self.matrix[y][0] = "X"
            self.matrix[y][-1] = "X"
            self.tiles[y][0].change_name(["wall.png"])
            self.tiles[y][-1].change_name(["wall.png"])
            
        
    def calc_image(self):
        
        super().calc_image()
        matrix_surface = pygame.Surface((self.width,self.height),pygame.SRCALPHA)
        for y in range(self.y_tiles):
            for x in range(self.x_tiles):
                matrix_surface.blit(self.tiles[y][x].image,self.tiles[y][x].rect)
        self.image.blit(matrix_surface,matrix_surface.get_rect(center=self.rect.center))


    def rescale(self,new_winsize):

        super().rescale(new_winsize)
        for y in range(self.y_tiles):
            for x in range(self.x_tiles):
                self.tiles[y][x].rescale(new_winsize)
        self.calc_image()

    
        
