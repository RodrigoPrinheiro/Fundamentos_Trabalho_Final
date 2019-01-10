import pygame, sys, random
from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('mov/cam reset')

# Set up the colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YEET = (255, 255, 0)

# Set up the player and food data structure.
player = pygame.Rect(190, 190, 10, 10)

# Set up movement variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 2

windowSurface.fill(BLUE)
windowSurface.fill(GREEN)
windowSurface.fill(RED)
windowSurface.fill(YEET)


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

    #draw bkacground
    windowSurface.fill(WHITE)

    
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
    if moveDown and player.bottom >= WINDOWHEIGHT:
        player.top = 0 + MOVESPEED
        windowSurface.fill(BLUE)
        screen = 0
    elif moveUp and player.top <= 0:
        player.bottom = WINDOWHEIGHT - MOVESPEED
        windowSurface.fill(GREEN)
        screen = 1
    elif moveLeft and player.left <= 0:
        player.right = WINDOWWIDTH - MOVESPEED
        screen = 2
        windowSurface.fill(RED)        
    elif moveRight and player.right >= WINDOWWIDTH:
        player.left = 0 + MOVESPEED
        screen = 3
        windowSurface.fill(YEET)
    else:
        windowSurface.fill(WHITE)

    # Draw the player onto the surface.
    pygame.draw.rect(windowSurface, BLACK, player)

    # Draw the window onto the screen.
    pygame.display.update()
    mainClock.tick(40 )
