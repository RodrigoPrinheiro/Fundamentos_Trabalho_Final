import pygame
import playerObject, gameObjects
GREY = (100,100,100)
GREEN = (0,128,0)
BLACK = (0,0,0)
class Game(object):
    def __init__(self):
        self.menu = False
        
        #Criar lista de sprites um para todos e outro para varios objetos iguais
        #Criar mais e agrupar objetos iguais quando se adicionar mais
        self.all_sprite_list = pygame.sprite.Group()
        self.rock_list = pygame.sprite.Group()

        rock = gameObjects.Rock()
        self.rock_list.add(rock)
        self.all_sprite_list.add(rock)
        
        self.player = playerObject.Player()
        self.all_sprite_list.add(self.player)
    
    def process_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return True
            if event.type == MOUSEBUTTONDOWN:
                if self.menu: #comecar e dar reset do jogo
                    self.__init__()
            if event.type == KEYDOWN:
                #andar para cima
                if event.key == K_UP:
                    moveU = True
                    moveD = moveL = moveR = False
                #ANDAR PARA BAIXO
                elif event.key == K_DOWN:
                    moveD = True
                    moveU = moveR = moveL = False
                #ANDAR PARA A ESQUERDA
                elif event.key == K_LEFT:
                    moveL = True
                    moveU = moveR =moveD = False
                #ANDAR PARA A DIREITA
                elif event.key == K_RIGHT:
                    moveR = True
                    moveD = moveU = moveL = False
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                if event.key == K_DOWN:
                    moveD = False
                elif event.key == K_LEFT:
                    moveL = False
                elif event.key == K_UP:
                    moveU = False
                elif event.key == K_RIGHT:
                    moveR = False
        if moveU:
            self.rect.move_ip(0, -1* self.moveSpeed)
        elif moveD:
            self.rect.move_ip(0, self.moveSpeed)
        elif moveL:
            self.rect.move_ip(-1 * self.moveSpeed)
        elif moveR:
            self.rect.move_ip(self.moveSpeed, 0)

    def game_logic(self):
        #corre a cada frame, da update das posicoes e procura por colisoes 
        if not self.menu:
            self.all_sprite_list.update()
            #lista a cada frame com os objetos que estao a colidir com o jogador
            rock_hit_list = pygame.sprite.spritecollide(self.player, self.rock_list, True)
            #fazer por objeto da lista um comando
            for rock in rock_hit_list:
                self.posDif = rock.moveRelative(self.player)
                self.player.rect.move_ip(posDif)
    def display_new_frame(self, screen):
        screen.fill(GREEN)

        if self.menu:
            #setup menu, fazer depois
            screen.fill(BLACK)
        if not self.menu:
            #atualizar tudo oque foi mudado, oque nao mudou de posicao nao e updated
            self.all_sprites_list.draw(screen)

        pygame.display.flip()#desenhar frame