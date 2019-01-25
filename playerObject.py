import pygame
import math
from settings import *
#TUDO DO JOGADOR ENCONTRA SE AQUI, CLASS, ONDE SE IMPORTA O SPRITE ETC...

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/res/resDown.png").convert_alpha() #SPRITE SHEET é suposto ser overwritten for now
        self.image = pygame.image.load("Sprites/WIP/res/resStill.png").convert_alpha() #load sprite image here plz
        self.image = pygame.transform.scale(self.image, (52, 52)) # mudar o tamanho do sprite, 52x52 looks good to me
        self.rect = self.image.get_rect()#tirar um rectangulo do sprite
        self.rect.center = (50, 50)
        self.has_KEY = False

    def animation(self):
        print('.')

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x -= PLAYERSPEED
        if keystate[pygame.K_RIGHT]:
            self.rect.x += PLAYERSPEED
        if keystate[pygame.K_UP]:
            self.rect.y -= PLAYERSPEED
        if keystate[pygame.K_DOWN]:
            self.rect.y += PLAYERSPEED
        
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WINDOWHEIGHT:
            self.rect.bottom = WINDOWHEIGHT
