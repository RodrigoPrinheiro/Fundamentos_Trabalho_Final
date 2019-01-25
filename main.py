import pygame, sys, random
from pygame.locals import *
import playerObject, gameObjects
import os

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

zona1_1 = pygame.image.load("sprites/WIP/zona_1_1/zona_1_1_unfinished.gif").convert_alpha()
zona1_1 = pygame.transform.scale(zona1_1, (1280, 720))

# Set up the colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YEET = (255, 255, 0)

#Set up assets
"""EXEMPLO DE COMO DAR PROPER LOAD DE IMAGENS PARA PYGAME (OPTIMIZACAO)>>>
someObject()

    self.image = pygame.image.load("path/"image.png").convert_alpha()    """

# Set up variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

"""#TEMP THIS GONNA BE A CLASS VVVV this doesnt work as a class, WIDTH e a HEIGHT deve ser sempre variavel normal nao class
dont dump out classes just because, they are needed if its an object, like a key, a block, the player. not the screen.
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

"""grupo de sprites, adicionar o objeto a este grupo como esta exemplificado no player,
ATENCAO VER PLAYER CLASS E COMO ESTA DECLARADA, IMPORTANTE PARA FUNCIONAR"""

all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
keys = pygame.sprite.Group()

yellowKey = gameObjects.Key()
all_sprites.add(yellowKey)
keys.add(yellowKey)

rock = gameObjects.Rock()
all_sprites.add(rock)
rocks.add(rock)

player = playerObject.Player()
all_sprites.add(player)

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
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


    if player.rect.left <= 0:
        currentArea += 1
        player.rect.right = WINDOWWIDTH
    elif player.rect.right >= WINDOWWIDTH and currentArea != 0:
        currentArea -= 1
        player.rect.left = 0

    #update
    all_sprites.update() #updates ALL SPRITES positions without clogging up with multiple background repeats

    #check for colisions here
    hits = pygame.sprite.spritecollide(player, rocks, False)
    if hits:
        rock.moveRelative(player)
    #Draw the ALL SPRITES on surface.
    if currentArea <= 0:
        screen.blit(zona1,(0,0))
    elif currentArea == 1:
        screen.blit(zona1_1,(0,0))
    elif currentArea == 2:
        screen.blit(zona2,(0,0))
    else:
        windowSurface.fill(GREEN)

    all_sprites.draw(windowSurface)
    """screen.blit(zona1_1,(0,0),(cImage*w,0,w,h))"""

    # commit render
    pygame.display.flip()
    mainClock.tick(60)
