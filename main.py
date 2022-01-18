import pygame
from tile import *

#initialize pygame
pygame.init()

#creating a screen
#(width, height)
screen = pygame.display.set_mode((500,500))

#adding title, icon and background to the screen
pygame.display.set_caption("I Love Hue")
gameicon = pygame.image.load("ilovehue.png")
pygame.display.set_icon(gameicon)
background = (0,0,0)
screen.fill(background)

#creating color palette
icolor = [250,0,50]
hchange = [-50,0,0]
vchange = [0,0,50]

xstart = 0
ystart = 0

# 250,0,50     200,0,50     150,0,50     100,0,50     50,0,50
# 250,0,100    200,0,100    150,0,100    100,0,100    50,0,100
# 250,0,150    200,0,150    150,0,150    100,0,150    50,0,150
# 250,0,200    200,0,200    150,0,200    100,0,200    50,0,200
# 250,0,250    200,0,250    150,0,250    100,0,250    50,0,250

#creating tiles
all_sprites_list = pygame.sprite.Group()

ytile=ystart
vcolor = icolor
while (ytile<500):
    xtile=xstart
    hcolor = vcolor
    while (xtile<500):
        tile_col = tuple(hcolor)
        
        t1 = Tile(tile_col)
        t1.rect.x = xtile
        t1.rect.y = ytile
        all_sprites_list.add(t1)
        xtile = xtile+WIDTH
        hcolor = [x1 + x2 for x1,x2 in zip(hcolor,hchange)]
        
    
    ytile+=HEIGHT
    vcolor = [x1 + x2 for x1,x2 in zip(vcolor,vchange)]

running = True
while running:

    for event in pygame.event.get():

        #quits the game when the cross button is clicked
        if event.type == pygame.QUIT:
            running = False
    
    
    all_sprites_list.update()
    screen.fill(background)
    all_sprites_list.draw(screen)
    pygame.display.flip()