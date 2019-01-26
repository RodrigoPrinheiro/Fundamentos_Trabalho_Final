import pygame
import math
from settings import *
#TUDO DO JOGADOR ENCONTRA SE AQUI, CLASS, ONDE SE IMPORTA O SPRITE ETC...

class Player(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("Sprites/res/resDown.png")
        self.image = pygame.transform.scale(self.image, (1144, 52))
        
        self.imageStill = pygame.image.load("Sprites/res/resStill.png")
        self.imageStill = pygame.transform.scale(self.imageStill, (52, 52))

        self.screen=screen
  
        self.nImg=22 #number of sprites
        self.cImg=0 #current sprite

        self.w = 52 #sprite size x
        self.h = 52 #sprite size y

        self.rect = self.imageStill.get_rect()#tirar um rectangulo do sprite
        self.rect.center = (80, 150)
        self.has_KEY = False


    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and self.rect.x >= 10:
            self.rect.x -= PLAYERSPEED
        if keystate[pygame.K_RIGHT] and self.rect.x <= WINDOWWIDTH - self.w - 20:
            self.rect.x += PLAYERSPEED
        if keystate[pygame.K_UP] and self.rect.y >= 70:
            self.rect.y -= PLAYERSPEED
        if keystate[pygame.K_DOWN] and self.rect.y <= WINDOWHEIGHT - self.h - 20:
            self.rect.y += PLAYERSPEED
        
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WINDOWHEIGHT:
            self.rect.bottom = WINDOWHEIGHT

        #ANIMATION vvvvvvvvvvvvvvvv
        if keystate[pygame.K_LEFT] == True or keystate[pygame.K_RIGHT] == True or keystate[pygame.K_UP] == True or keystate[pygame.K_DOWN] == True:
        
            if self.cImg >=self.nImg-1:
                self.cImg = 0
            else:
                self.cImg+= 1

        self.screen.blit(self.image,self.rect,(self.cImg*self.w,0,self.w,self.h))

