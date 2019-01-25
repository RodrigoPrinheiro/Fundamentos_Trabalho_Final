import pygame
import math
#TUDO DO JOGADOR ENCONTRA SE AQUI, CLASS, ONDE SE IMPORTA O SPRITE ETC...
WINDOWWIDTH = 1280
WINDOWHEIGHT = 720
RED = (255,0,0)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20)) #load sprite image here plz
        self.image.fill(RED) #remmover quando tivermos sprite
        self.rect = self.image.get_rect()#tirar um rectangulo do sprite
        self.rect.center = ( 2, 2)


    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 5
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 5
        if keystate[pygame.K_UP]:
            self.rect.y -= 5
        if keystate[pygame.K_DOWN]:
            self.rect.y += 5
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOWWIDTH:
            self.rect.right = WINDOWWIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WINDOWHEIGHT:
            self.rect.bottom = WINDOWHEIGHT
