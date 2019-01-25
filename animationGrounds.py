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

#zona1 = pygame.image.load("Sprites/WIP/zona_1/zona_1_unfinished.png").convert_alpha()
#zona1 = pygame.transform.scale(zona1, (1280, 720))

zona2 = pygame.image.load("Sprites/WIP/zona_2/zona_2_unfinished.png").convert_alpha()
zona2 = pygame.transform.scale(zona2, (1280, 720))

zona1_1 = pygame.image.load("Sprites/WIP/zona_1_1/zona_1_1_unfinished.gif").convert_alpha()
zona1_1 = pygame.transform.scale(zona1_1, (1280, 720))

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

yellowKey = gameObjects.Key()
all_sprites.add(yellowKey)
keys.add(yellowKey)

rock = gameObjects.Rock()
all_sprites.add(rock)
rocks.add(rock)

player = playerObject.Player()
all_sprites.add(player)

class Animation:
    def __init__(self):
        self.images=pygame.image.load("Sprites/res/resDown.png")
        self.images = pygame.transform.scale(self.images, (1144, 52))
        660
        self.nImg=22 #number of sprites
        self.cImg=0 #current sprite

        self.x= 200
        self.y= 200

        self.w = 52 
        self.h = 52

    def update(self):
        if self.cImg >=self.nImg-1:
            self.cImg = 0
        else:
            self.cImg+= 1


    def render(self,screen):
        # reminder: pygame.Rect(WINDOWWIDTH-400, WINDOWHEIGHT -950, 130, 100)
        
        #pygame.draw.rect(screen,RED,self.rect)
        screen.blit(self.images,(self.x,self.y),(self.cImg*self.w,0,self.w,self.h))


animation = Animation()


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


    if player.has_KEY == True:
        door1.kill()
        player.has_KEY = False

    if player.rect.left <= 0:
        currentArea += 1
        player.rect.right = WINDOWWIDTH
    elif player.rect.right >= WINDOWWIDTH and currentArea != 0:
        currentArea -= 1
        player.rect.left = 0


    #update
    all_sprites.update() #updates ALL SPRITES positions without clogging up with multiple background repeats

    #check for colisions here
    if pygame.sprite.spritecollide(player, rocks, False): #escadas?
        player.rect.x -= PLAYERSPEED
        player.rect.y -= PLAYERSPEED

    if pygame.sprite.spritecollide(player, doors, False):
        player.rect.x += PLAYERSPEED

    hits = pygame.sprite.spritecollide(player, keys, True)
    if hits:
        player.has_KEY = True
        #hits[0].kill()

    hits = pygame.sprite.spritecollide(player, walls, False)
    if hits:
        if hits[0].rect.x > WINDOWWIDTH /2:
            player.rect.x -= PLAYERSPEED
        else:
            player.rect.x += PLAYERSPEED

    #Draw the ALL SPRITES on surface.
    if currentArea <= 0:
        windowSurface.fill(BLUE)
    elif currentArea == 1:
        windowSurface.fill(BLUE)
    elif currentArea == 2:
        screen.blit(zona2,(0,0))
    else:
        windowSurface.fill(BLUE)

    all_sprites.draw(windowSurface)
    """screen.blit(zona1_1,(0,0),(cImage*w,0,w,h))"""


    animation.update()
    animation.render(screen)

    # commit render
    pygame.display.flip()
    mainClock.tick(FPS)
    dlt = mainClock.tick(FPS) / 1000

