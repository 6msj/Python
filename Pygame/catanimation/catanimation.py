import pygame, sys
from pygame.locals import*

pygame.init()

FPS= 30 # frames per seconds setting
fpsClock = pygame.time.Clock()

#sets up the window
DISPLAY = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
cattyimg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

while True: # main game loop
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    DISPLAY.blit(cattyimg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)












