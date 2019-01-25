import pygame
import math
#OBJETOS DO JOGO, SPRITES ETC... ROCHAS, PONTES OBJETOS EM GERAL QUE SE PODE COLIDIR
GREY = (100,100,100)
YEET = (255, 255, 0)

WINDOWWIDTH = 1280
WINDOWHEIGHT = 720
class Door(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5,20))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.center = (0, WINDOWHEIGHT / 2)

class Key(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.image.fill(YEET)
        self.rect = self.image.get_rect()
        self.rect.center = (10, WINDOWHEIGHT / 2)

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)

    #mover objeto relativo a este (impedir de passar por ele)

    def moveRelative(self,other,speed = 5):
        #This function is a function the one you need uses, which you may find useful.
        #It is designed to move towards or a way from another sprite.
        #Other is the other sprite, speed is an integer, where a negative value specifies moving away from the sprite,
        #which is how many pixels it will move away from the target.
        #This returns coordinates for the move_ip function to move to or away from the sprite, as a tuple

        #other--- Objeto que queres colidir com (tem de estar em class com componente rect)
        #speed--- Como o objeto responde a colisao, valor negativo(valor inteiro). SE NAO METERES O SPEED SERA ATRIBUIDO O VALOR BASE DE 3(Player base speed)
        #retorna coordenadas para a funcao move_ip

        dx = other.rect.x - self.rect.x
        dy = other.rect.y - self.rect.y
        if abs(dx) > abs(dy):
        # other is farther away in x than in y
            if dx > 0:
                #devolve a velocidade que tem que mover no x para nao sair do sitio
                return (+speed,0)
            else:
                return (-speed,0)
        else:
            if dy > 0:
                #devolve a velocidade em y para nao mover do sitio
                return (0,+speed)
            else:
                return (0,-speed)
