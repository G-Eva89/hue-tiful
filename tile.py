import pygame

SURFACE_COLOR = (0,0,0)
HEIGHT = 100
WIDTH = 100

class Tile(pygame.sprite.Sprite):
    
    def __init__(self, color):
        super().__init__()
        
        self.color = color
        # self.mark = 1
        self.image = pygame.Surface((HEIGHT,WIDTH))
        self.image.fill(SURFACE_COLOR)

        pygame.draw.rect(self.image,self.color,pygame.Rect(0, 0, HEIGHT, WIDTH))
        self.rect = self.image.get_rect()