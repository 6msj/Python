import pygame, sys
from pygame.locals import*

pygame.init()
DISPLAY = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World!')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontobj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontobj.render('Hello World!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True: # main game loop
    DISPLAY.fill(BLACK)
    DISPLAY.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
