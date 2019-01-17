import pygame, sys, random
from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 1280
WINDOWHEIGHT = 720
size = (WINDOWWIDTH, WINDOWHEIGHT)
screen = pygame.display.set_mode(size)

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('movement/testing_grounds OuO')

zona1 = pygame.image.load("sprites/WIP/zona_1/zona_1_unfinished.png").convert_alpha()
zona1 = pygame.transform.scale(zona1, (1280, 720))

zona2 = pygame.image.load("sprites/WIP/zona_2/zona_2_unfinished.png").convert_alpha()
zona2 = pygame.transform.scale(zona2, (1280, 720))

zona1_1 = pygame.image.load("sprites/WIP/zona_1_1/zona_1_1_unfinished.gif")
zona1_1 = pygame.transform.scale(zona1_1, (1280, 720))

# Set up the colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YEET = (255, 255, 0)

# Set up the player RECT.
player = pygame.Rect(190, 190, 10, 10)

# Set up variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 8

"""#TEMP THIS GONNA BE A CLASS VVVV
numImages = 8
imageDelay = 0
h=720
w=1280
cImage = 0
NumImages = 15
ImageDelay = 0
################################NOT WORKING"""

currentArea = 0
    #0 - Zona 1
    #1 - Zona 1.1
    #2 - Zona 2
    #3 - Zona 2.1

windowSurface.fill(BLUE)
windowSurface.fill(GREEN)
windowSurface.fill(RED)
windowSurface.fill(YEET)



"""
if cImage==3: #reset the counter when walk
    imageDelay+=1
    if imageDelay >= 60-52:
        imageDelay = 0 
        cImage = 0
        
    else: #anim
        imageDelay+=1
        if imageDelay >= 60-52:
            imageDelay = 0 
            cImage+=1


NOT WORKING"""


# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        windowSurface.fill(WHITE)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)

    # Move the player.
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED
        
    #camera repositioning
    if moveLeft and player.left <= 0:
        currentArea += 1
        player.right = WINDOWWIDTH - MOVESPEED       
    elif moveRight and player.right >= WINDOWWIDTH and currentArea != 0:
        currentArea -= 1
        player.left = 0 + MOVESPEED

    # Draw the player and surface.
    if currentArea <= 0:
        screen.blit(zona1,(0,0))
    elif currentArea == 1:
        screen.blit(zona1_1,(0,0))
    elif currentArea == 2:
        screen.blit(zona2,(0,0))
    else:
        windowSurface.fill(GREEN)
           
    pygame.draw.rect(windowSurface, BLACK, player)
    """screen.blit(zona1_1,(0,0),(cImage*w,0,w,h))"""

    # Updating.
    pygame.display.update()
    mainClock.tick(60)
