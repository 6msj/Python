import pygame, sys
from pygame.locals import*

pygame.init()
DISPLAY = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World')

BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
RED = (255,0,0)

word = "Hello World!"

font_object = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = font_object.render(word, True, RED, BLUE)
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


## Loading and playing a sound effect:
#soundObj = pygame.mixer.Sound('beepingsound.wav')
#soundObj.play()
#
## Loading and playing background music:
#pygame.mixer.music.load(backgroundmusic.mp3')
#pygame.mixer.music.play(-1, 0.0)
## ...some more of your code goes here...
#pygame.mixer.music.stop()
