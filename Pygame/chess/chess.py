import pygame, sys
from pygame.locals import*

# colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 128)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
WHITE = (255, 255, 255)
GREY = (119, 136, 153)
BROWN = (92, 51, 23)
LIGHTSTEELBLUE = (84,84,84 )
BGCOLOR = BLACK
TILECOLOR = WHITE

# dimensions
WINHEIGHT = 600
WINWIDTH = 600
NUMCOLUMNS = 8
NUMROWS = 8
DRAWINGBOXES = 4
RADIUS = 25

BOXSIZE = WINHEIGHT / NUMCOLUMNS

def drawBoard(): # draws the chess board
    for i in range (DRAWINGBOXES):
        for j in range (DRAWINGBOXES):
            pygame.draw.rect(DISPLAYSURF, TILECOLOR, (2*i*BOXSIZE, 2*j*BOXSIZE, BOXSIZE, BOXSIZE))
            #circle_x = (2*i*BOXSIZE)+RADIUS
            #circle_y= (2*j*BOXSIZE)-RADIUS
            #pygame.draw.circle(DISPLAYSURF, BLUE, (int(circle_x), int(circle_y)), RADIUS, 0)

    for i in range (DRAWINGBOXES):
        for j in range (DRAWINGBOXES):
            pygame.draw.rect(DISPLAYSURF, TILECOLOR, (BOXSIZE+(i*BOXSIZE*2), BOXSIZE+(j*BOXSIZE*2), BOXSIZE, BOXSIZE))
            #circle_x = (BOXSIZE+(i*BOXSIZE*2)+RADIUS)
            #circle_y = (BOXSIZE+(j*BOXSIZE*2)-RADIUS)
            #pygame.draw.circle(DISPLAYSURF, BLUE, (int(circle_x), int(circle_y)), RADIUS, 0)

#def drawPieces():
    #rook = pygame.image.load('rook.jpg')
    #DISPLAYSURF.blit(rook, (0, 0))

#draw a circle around a point
#pygame.draw.circle(Surface, color, pos, radius, width=0): return Rect

#Draws a circular shape on the Surface. The pos argument is the center of the circle, and radius is the size. The width argument is the thickness to draw the outer edge. If width is zero then the circle will be filled.


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

    pygame.display.set_caption('Chess Board')

    DISPLAYSURF.fill(BGCOLOR)
    while True: # main game loop
        DISPLAYSURF.fill(BLACK) # drawing the window
        drawBoard()
        #drawPieces()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

# runs the game
if __name__=='__main__':
    main()
