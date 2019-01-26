import pygame
import math
from settings import *
#OBJETOS DO JOGO, SPRITES ETC... ROCHAS, PONTES OBJETOS EM GERAL QUE SE PODE COLIDIR

class Door(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,500))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)


class Key(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(YEET)
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOWWIDTH /2 + 100, WINDOWHEIGHT / 2)

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1,WINDOWHEIGHT))
        self.rect = self.image.get_rect()
        self.image.fill(YEET)

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1000,50))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.center = (20, 260)
        
