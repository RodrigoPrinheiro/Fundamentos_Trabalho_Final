import pygame
import math
import gameObjects
#TUDO DO JOGADOR ENCONTRA SE AQUI, CLASS, ONDE SE IMPORTA O SPRITE ETC...
RED = (255,0,0)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.Sprite = pygame.surface([20,40]) #load sprite here plz
        self.Sprite =Sprite.fill(RED) #remmover quando tivermos sprite
        self.moveSpeed = 3 #velocidade do player
        self.rect = Sprite.get_rect()#tirar um rectangulo do sprite

    def resetPos(self):
        self.rect.x = 1280/2
        self.rect.y = 720/2
    
    def moveRelative(self,other,speed = 3): #This function is a function the one you need uses, which you may find useful. It is designed to move towards or a way from another sprite. Other is the other sprite, speed is an integer, where a negative value specifies moving away from the sprite, which is how many pixels it will move away from the target. This returns coordinates for the move_ip function to move to or away from the sprite, as a tuple
           
        #other--- Objeto que queres colidir com (tem de estar em class com componente rect)
        #speed--- Como o objeto responde a colisao, valor negativo(valor inteiro)SE NAO METERES O SPEED SERA ATRIBUIDO O VALOR BASE DE 3(Player base speed)
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


    def move(self,dx,dy):
            screen.fill((COLOR),self.rect)       #covers over the sprite's rectangle with the background color, a constant in the program
            collisions = pygame.sprite.spritecollide(self, everything, False)
            for other in collisions:
                    if other != self:
                            (awayDx,awayDy) = self.moveRelative(other,-1)  #moves away from the object it is colliding with
                            dx = dx + 9*(awayDx)                           #the number 9 here represents the object's resistance. When you push on an object, it will push with a force of nine back. If you make it too low, players can walk right through other objects. If you make it too high, players will bounce back from other objects violently upon contact. In this, if a player moves in a direction faster than a speed of nine, they will push through the other object (or simply push the other object back if they are also in motion)
                            dy = dy + 9*(awayDy)        