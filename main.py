import pygame, sys, random
from pygame.locals import *
from settings import *
import playerObject, gameObjects
import os

# Set up pygame
pygame.mixer.pre_init(44100,-16,2,1024)#preload dos sons
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
thumpSound = pygame.mixer.Sound('Sounds/fall.wav')

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

player = playerObject.Player(screen)

"PARA A ZONA_1"
all_sprites = pygame.sprite.Group()
rocksU = pygame.sprite.Group()
rocksD = pygame.sprite.Group()
rocksL = pygame.sprite.Group()
rocksR = pygame.sprite.Group()
keys = pygame.sprite.Group()
doors = pygame.sprite.Group()
walls = pygame.sprite.Group()

door1 = gameObjects.Door()
all_sprites.add(door1)
doors.add(door1)

wall = gameObjects.Wall()
all_sprites.add(wall)
walls.add(wall)
wall.rect.topleft = (30, 300)

yellowKey = gameObjects.Key(screen)
all_sprites.add(yellowKey)
keys.add(yellowKey)

rockU = gameObjects.Rock()#queda para cima orginal
all_sprites.add(rockU)
rocksU.add(rockU)

rockD = gameObjects.Rock()#queda para baixo original
all_sprites.add(rockD)
rocksD.add(rockD)
rockD.rect.center = (280, 265)

rockL = gameObjects.RockH()#queda para esquerda original
all_sprites.add(rockL)
rocksL.add(rockL)
rockL.rect.topleft = (535,265)

rockR = gameObjects.RockH()#queda para direita original
all_sprites.add(rockR)
rocksR.add(rockR)
rockR.rect.topleft = (520,270)

rockU2 = gameObjects.Rock()
all_sprites.add(rockU2)
rocksU.add(rockU2)
rockU2.rect.center = (800, 435)

rockD2 = gameObjects.Rock()
all_sprites.add(rockD2)
rocksD.add(rockD2)
rockD2.rect.center = (800, 440)

rockL2 = gameObjects.RockH()
all_sprites.add(rockL2)
rocksL.add(rockL2)
rockL2.rect.topleft = (800,55)

rockR2 = gameObjects.RockH()
all_sprites.add(rockR2)
rocksR.add(rockR2)
rockR2.rect.topleft = (775,55)

rockL3 = gameObjects.RockH()
all_sprites.add(rockL3)
rocksL.add(rockL3)
rockL3.rect.topleft = (1050,245)

rockR3 = gameObjects.RockH()
all_sprites.add(rockR3)
rocksR.add(rockR3)
rockR3.rect.topleft = (1020,245)

stalker_1 = gameObjects.Stalker(screen)
stalker_1.rect.center = (300,WINDOWHEIGHT-270)

stalker_2 = gameObjects.Stalker(screen)
stalker_2.rect.center = (WINDOWWIDTH - 100,100)

plant = gameObjects.Decor(screen,FPS)

"PARA A ZONA_2"
all_sprites2 = pygame.sprite.Group()
rocksUZ2 = pygame.sprite.Group()
rocksDZ2 = pygame.sprite.Group()
rocksLZ2 = pygame.sprite.Group()
rocksRZ2 = pygame.sprite.Group()
keysZ2 = pygame.sprite.Group()
doorsZ2 = pygame.sprite.Group()
wallsZ2 = pygame.sprite.Group()

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
    #all_sprites.update() #updates ALL SPRITES positions without clogging up with multiple background repeats


    #Draw the ALL SPRITES on surface.
    if currentArea <= 0:
        screen.blit(zona1,(0,0))
    elif currentArea == 1:
        screen.blit(zona1_1,(0,0))
    elif currentArea == 2:
        screen.blit(zona2,(0,0))
    else:
        windowSurface.fill(GREEN)

    if currentArea == 0:         
        #check for colisions here
        if pygame.sprite.spritecollide(player, rocksU, False):
            player.rect.y -= 75
            thumpSound.play()
        if pygame.sprite.spritecollide(player, rocksD, False):
            player.rect.y += 75
            thumpSound.play()
        if pygame.sprite.spritecollide(player, rocksL, False):
            player.rect.x += 75
            thumpSound.play()
        if pygame.sprite.spritecollide(player, rocksR, False):
            player.rect.x -= 75
            thumpSound.play()
        
        #inimigos a cair tb############
        if pygame.sprite.spritecollide(stalker_1, rocksU, False):
            stalker_1.rect.y -= 15
        if pygame.sprite.spritecollide(stalker_1, rocksD, False):
            stalker_1.rect.y += 15
        if pygame.sprite.spritecollide(stalker_1, rocksL, False):
            stalker_1.rect.x += 15
        if pygame.sprite.spritecollide(stalker_1, rocksR, False):
            stalker_1.rect.x -= 15    
            
        if pygame.sprite.spritecollide(stalker_1, rocksU, False):
            stalker_2.rect.y -= 15
        if pygame.sprite.spritecollide(stalker_1, rocksD, False):
            stalker_2.rect.y += 15
        if pygame.sprite.spritecollide(stalker_2, rocksL, False):
            stalker_2.rect.x += 15
        if pygame.sprite.spritecollide(stalker_2, rocksR, False):
            stalker_2.rect.x -= 15 

        #if mais inimigos oof do this 
        ###############################
            
        if pygame.sprite.spritecollide(player, doors, False):
            player.rect.x += PLAYERSPEED

        hits = pygame.sprite.spritecollide(player, keys, True)
        if hits:
            player.has_KEY = True
            #hits[0].kill()

        #contacto com o totem
        if pygame.sprite.spritecollide(player, walls, False):
            player.rect.x += PLAYERSPEED
            player.rect.y += PLAYERSPEED 

        #all_sprites.draw(windowSurface)

        # commit render
        plant.update()
        
        if player.has_KEY == True:
            yellowKey.exists = False      
        if yellowKey.exists == True:
            yellowKey.updateSprite()

        stalker_1.update(player,FPS)
        stalker_2.update(player,FPS)

        
    elif currentArea == 2:
        print
        #all_sprites.draw(windowSurface)
        #all_sprites.update()
        
    player.update()
    
    pygame.display.flip()
    mainClock.tick(FPS)
    dlt = mainClock.tick(FPS) / 1000
