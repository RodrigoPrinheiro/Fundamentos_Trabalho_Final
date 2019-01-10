import pygame
import math
import gameObjects, playerObject
from GameLogic import Game

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
def main():
    #funcao main do jogo
    #inicializar tudo
    pygame.init()
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    
    pygame.display.caption = "Lucern"
    pygame.mouse.set_visible(False)

    #Instanciar o jogo
    game = Game()

    done = False
    clock = pygame.time.clock()
    #Main loop

    while not done:
        #faz oque diz
        game.process_events()
        #update de posicoes dos objetos
        game.game_logic()
        #desenhar a nova frame
        game.display_new_frame(screen)
        #frame rate
        clock.tick(75)
    pygame.quit

if __name__ == "__main__":
    main()