import pygame, sys, random
from pygame.locals import *
from settings import *
import playerObject, gameObjects
import os

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

size = (WINDOWWIDTH, WINDOWHEIGHT)
screen = pygame.display.set_mode(size)

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption(TITLE)


zona1 = pygame.image.load("Sprites/WIP/zona_1/zona_1_unfinished.png").convert_alpha()
zona1 = pygame.transform.scale(zona1, (1280, 720))

zona2 = pygame.image.load("Sprites/WIP/zona_2/zona_2_unfinished.png").convert_alpha()
zona2 = pygame.transform.scale(zona2, (1280, 720))

zona1_1 = pygame.image.load("Sprites/WIP/zona_1_1/zona_1_1_unfinished.gif").convert_alpha()
zona1_1 = pygame.transform.scale(zona1_1, (1280, 720))

#music/sounds
music = pygame.mixer.music.load('Sounds/bgmusic.wav')
pygame.mixer.music.play(-1)
doorSound = pygame.mixer.Sound('Sounds/door.wav')
#not working
walkSound = pygame.mixer.Sound('Sounds/walk.wav')

#Set up assets
"""EXEMPLO DE COMO DAR PROPER LOAD DE IMAGENS PARA PYGAME (OPTIMIZACAO)>>>
someObject()

    self.image = pygame.image.load("path/"image.png").convert_alpha()    """

# Set up variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

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
doors = pygame.sprite.Group()
walls = pygame.sprite.Group()

door1 = gameObjects.Door()
all_sprites.add(door1)
doors.add(door1)

wall = gameObjects.Wall()
all_sprites.add(wall)
walls.add(wall)
wall.rect.top = door1.rect.bottom

wall2 = gameObjects.Wall()
all_sprites.add(wall2)
walls.add(wall2)
wall2.rect.bottom = door1.rect.top

yellowKey = gameObjects.Key(screen)
all_sprites.add(yellowKey)
keys.add(yellowKey)

rock = gameObjects.Rock()
all_sprites.add(rock)
rocks.add(rock)

player = playerObject.Player(screen)


stalker_1=gameObjects.Stalker(screen)
stalker_1.rect.center = (300,WINDOWHEIGHT-270)

stalker_2=gameObjects.Stalker(screen)
stalker_2.rect.center = (WINDOWWIDTH - 100,100)



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

    if PLAYERSPEED > 0 and PLAYERSPEED < 0:
        walkSound.play()
    if player.has_KEY == True: 
        door1.kill()
        doorSound.play()
        player.has_KEY = False

    if player.rect.left <= 10 and player.rect.top < 250 and player.rect.top > 0:
        currentArea = 2
        player.rect.right = WINDOWWIDTH -1 - player.w
    elif player.rect.right >= WINDOWWIDTH - 20  and player.rect.top < 259 and player.rect.top > 0 and currentArea != 0:
        currentArea = 0 
        player.rect.left = 80
        player.rect.top = 150
    
    #update
    all_sprites.update() #updates ALL SPRITES positions without clogging up with multiple background repeats
            
    #check for colisions here
    if pygame.sprite.spritecollide(player, rocks, False):
        player.rect.y -= 75
        #INSERT FALLSOUND.PLAY

    #inimigos a cair tb############
    if pygame.sprite.spritecollide(stalker_1, rocks, False):
        stalker_1.rect.y -= 75

    #if mais inimigos oof do this 
    ###############################
        
    if pygame.sprite.spritecollide(player, doors, False):
        player.rect.x += PLAYERSPEED

    hits = pygame.sprite.spritecollide(player, keys, True)
    if hits:
        player.has_KEY = True
        #hits[0].kill()

    #hits = pygame.sprite.spritecollide(player, walls, False)
    #if hits:
        #if hits[0].rect.x > WINDOWWIDTH /2:
            #player.rect.x -= PLAYERSPEED
        #else:
            #player.rect.x += PLAYERSPEED

    #Draw the ALL SPRITES on surface.
    if currentArea <= 0:
        screen.blit(zona1,(0,0))
    elif currentArea == 1:
        screen.blit(zona1_1,(0,0))
    elif currentArea == 2:
        screen.blit(zona2,(0,0))
    else:
        windowSurface.fill(GREEN)

    #all_sprites.draw(windowSurface)

    # commit render
    player.update()

    stalker_1.update(player,FPS)
    stalker_2.update(player,FPS)

    if player.has_KEY == True:
        yellowKey.exists = False      
    if yellowKey.exists == True:
        yellowKey.updateSprite()
    
    pygame.display.flip()
    mainClock.tick(FPS)
    dlt = mainClock.tick(FPS) / 1000
