import pygame, random
import math
from settings import *

class Decor(pygame.sprite.Sprite):
    def __init__(self,screen,FPS):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((26,29))
        self.image=pygame.image.load("Sprites/decor/plant.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, ((15*5)*3, 14*3))
        self.still=pygame.image.load("Sprites/decor/plantStill.png").convert_alpha()
        self.still = pygame.transform.scale(self.still,(15*3, 14*3))
        self.rect = self.still.get_rect()
        self.rect.center = (1050, 450)

        self.screen=screen
        self.FPS = FPS

        self.nImg=5 #number of sprites
        self.cImg=0 #current sprite
        
        self.totalDelay = 56 #tempo antes de mudar de sprite (Quanto maior mais lento)
        self.delay = 0 #contagem do delay usado no update

        self.w = 15*3 #sprite size x
        self.h = 14*3 #sprite size y

    def update(self):
        #ANIMATION vvvvvvvvvvvvvvvv
        if self.cImg >=self.nImg-1:
            self.delay += 1
            if self.delay == self.FPS-(self.totalDelay-44):#fazer o ultimo frame demorar mais (barely unnoticeable)
                self.cImg = 0
        else:
            if self.delay >= self.FPS-self.totalDelay:
                self.cImg+= 1
                self.delay=0
            else:
                self.delay+=1

        self.screen.blit(self.image,self.rect,(self.cImg*self.w,0,self.w,self.h))
        


class Door(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,150))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 170)


class Key(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((26,29))
        self.image=pygame.image.load("Sprites/key/keySheet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, ((26*12)*3, 29*3))
        self.still=pygame.image.load("Sprites/key/keyStill.png").convert_alpha()
        self.rect = self.still.get_rect()
        self.rect.center = (300, 360)
        self.exists = True

        self.screen=screen

        self.nImg=12 #number of sprites
        self.cImg=0 #current sprite
        
        self.totalDelay = 58 #tempo antes de mudar de sprite (Quanto maior mais lento)
        self.delay = 0 #contagem do delay usado no update

        self.w = 26*3 #sprite size x
        self.h = 29*3 #sprite size y

    def updateSprite(self):
        #ANIMATION vvvvvvvvvvvvvvvv
        if self.cImg >=self.nImg-1:
            self.delay += 1
            if self.delay == FPS-self.totalDelay:#fazer o ultimo frame demorar mais (barely unnoticeable)
                self.cImg = 0
        else:
            if self.delay == FPS-self.totalDelay:
                self.cImg+= 1
                self.delay=0
            else:
                self.delay+=1

        self.screen.blit(self.image,self.rect,(self.cImg*self.w,0,self.w,self.h))
        

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((110,90))
        self.image.set_alpha(250)
        self.rect = self.image.get_rect()

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((520,10))
        self.image.set_alpha(250)  
        self.rect = self.image.get_rect()
        self.rect.center = (280, 255)

class RockH(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,165))
        self.image.set_alpha(250)  
        self.rect = self.image.get_rect()
        self.rect.center = (280, 255)


class Stalker(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        
        self.stalkLeft=pygame.image.load("Sprites/enemies/stalkerLeft.png").convert_alpha()
        self.stalkLeft = pygame.transform.scale(self.stalkLeft, (140*4, 22*4))
        self.stalkRight=pygame.image.load("Sprites/enemies/stalkerRight.png").convert_alpha()
        self.stalkRight = pygame.transform.scale(self.stalkRight, (140*4, 22*4))
        
        self.image = self.stalkLeft
        
        self.imageStill = pygame.image.load("Sprites/enemies/stalkerStill.png").convert_alpha()
        self.imageStill = pygame.transform.scale(self.imageStill, (11*4, 20*4))

        self.screen=screen
  
        self.nImg=10 #number of sprites
        self.cImg=0 #current sprite
        
        self.totalDelay = 58 #tempo antes de mudar de sprite (Quanto maior mais lento)
        self.delay = 0 #contagem do delay usado no update

        self.w = 14*4 #sprite size x
        self.h = 22*4 #sprite size y

        self.rect = self.imageStill.get_rect()#tirar um rectangulo do sprite
        self.range = 350

    def update(self,player,FPS):
        if player.rect.x >= self.rect.x -self.range and player.rect.x <= self.rect.x +self.range and player.rect.y >= self.rect.y -(self.range-(int(self.range/3))) and player.rect.y <= self.rect.y +(self.range-(int(self.range/3))):
            if player.rect.x<self.rect.x: #esquerda
                self.rect.move_ip(-PLAYERSPEED+3,0)
                self.image=self.stalkLeft
            elif player.rect.x>self.rect.x: #direita
                self.rect.move_ip(PLAYERSPEED-3,0)
                self.image=self.stalkRight

            if player.rect.y<self.rect.y:
                self.rect.move_ip(0,-PLAYERSPEED+3)
            elif player.rect.y>self.rect.y:
                self.rect.move_ip(0,PLAYERSPEED-3)

            #ANIMATION vvvvvvvvvvvvvvvv
            if self.cImg >=self.nImg-1:
                self.delay += 1
                if self.delay == FPS-self.totalDelay:#fazer o ultimo frame demorar mais (barely unnoticeable)
                    self.cImg = 0
            else:
                if self.delay == FPS-self.totalDelay:
                    self.cImg+= 1
                    self.delay=0
                else:
                    self.delay+=1

            self.screen.blit(self.image,self.rect,(self.cImg*self.w,0,self.w,self.h))
            
        else:
            self.image = self.imageStill
            self.screen.blit(self.image,self.rect)


class Shooter(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        
        """self.stalkLeft=pygame.image.load("Sprites/enemies/stalkerLeft.png").convert_alpha()
        self.stalkLeft = pygame.transform.scale(self.stalkLeft, (140*4, 22*4))
        self.stalkRight=pygame.image.load("Sprites/enemies/stalkerRight.png").convert_alpha()
        self.stalkRight = pygame.transform.scale(self.stalkRight, (140*4, 22*4))
        
        self.image = self.stalkLeft
        
        self.imageStill = pygame.image.load("Sprites/enemies/stalkerStill.png").convert_alpha()
        self.imageStill = pygame.transform.scale(self.imageStill, (11*4, 20*4))
        """
        self.screen=screen
        """
        self.nImg=10 #number of sprites
        self.cImg=0 #current sprite
        
        self.totalDelay = 58 #tempo antes de mudar de sprite (Quanto maior mais lento)
        self.delay = 0 #contagem do delay usado no update

        self.w = 14*4 #sprite size x
        self.h = 22*4 #sprite size y

        self.rect = self.imageStill.get_rect()#tirar um rectangulo do sprite
        self.range = 350"""

        #shot properties
        self.shotSprite = pygame.image.load("Sprites/enemies/stalkerStill.png").convert_alpha()
        self.shotSprite = pygame.transform.scale(self.shotSprite, (11*4, 20*4))
        self.shots=[]
        self.shotMinSize = 199
        self.shotMaxSize = 200
        self.shotMinSpeed = 15
        self.shotMaxSpeed = 25
        self.shotAddRate = 50
        self.shotAddCounter = 0
        
    def update(self,player,FPS):
        #create the shot
        self.shotAddCounter+=1
        if self.shotAddCounter == self.shotAddRate:
            self.shotAddCounter = 0 #####pygame.Rect(random.randint(100, 200 - baddieSize)#####
            self.shotSize = random.randint(self.shotMinSize, self.shotMaxSize) #PYGAME.RECT((400,20, TAMANHO X SPRITE, TAMANHO Y SPRITE))
            self.newShot = {'rect': pygame.Rect(400,20, 11*4, 20*4), 
                        'speed': random.randint(self.shotMinSpeed, self.shotMaxSpeed),
                        'surface':pygame.transform.scale(self.shotSprite,(0,200)),
                        }
            self.shots.append(self.newShot)
        
        # Move the shots
        for b in self.shots: #change sides here (up down etc..)
               b['rect'].move_ip(0,b['speed'])

        #render them shots
        for b in self.shots:
            self.screen.blit(self.shotSprite,b['rect'])

        #collision
        for b in self.shots:
            if player.rect.colliderect(b['rect']):
                print('shot collide')

        """#ANIMATION vvvvvvvvvvvvvvvv
        if self.cImg >=self.nImg-1:
            self.delay += 1
            if self.delay == FPS-self.totalDelay:#fazer o ultimo frame demorar mais (barely unnoticeable)
                    self.cImg = 0
        else:
            if self.delay == FPS-self.totalDelay:
                    self.cImg+= 1
                    self.delay=0
            else:
                    self.delay+=1

        self.screen.blit(self.image,self.rect,(self.cImg*self.w,0,self.w,self.h))"""


