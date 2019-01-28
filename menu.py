import pygame
pygame.init()

WINDOWWIDTH = 1280
WINDOWHEIGHT = 720
win = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
win.fill((255,255,255))
def buttons():
    #class do butao de play
    class buttonP():
        def __init__(self, color, x,y,width,height,):
            self.color = color
            self.x = x
            self.y = y
            self.width = width
            self.height = height
        def draw(self,win,outline = None):
            #call this method to draw the button on the screen
            if outline:
                pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
                
            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)     
        def isOver(self, pos):
            #Pos is the mouse position or a tuple of (x,y) coordinates,isOver = está por cioma de
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True

    #class do butao de exit
    class buttonE():
        def __init__(self, color, x,y,width,height,):
            self.color = color
            self.x = x
            self.y = y
            self.width = width
            self.height = height
        def draw(self,win,outline = None):
            #call this method to draw the button on the screen
            if outline:
                pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
                
            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)     
        def isOver(self, pos):
            #Pos is the mouse position or a tuple of (x,y) coordinates,isOver = está por cioma de
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True


    #call para redesenhar janela
    def redrawWindow():
            win.fill((255,255,255))
            playButton.draw(win, (0,0,0))
            exitButton.draw(win, (0,0,0))

    run = True
    #play button
    playButton = buttonP((0,255,0), 515, 250, 250, 100)#por ordem - cor, X, Y, width, height
    exitButton = buttonE((0,0,255), 540, 370, 200, 80)#por ordem - cor, X, Y, width, height
    while run:
        redrawWindow()
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            #clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                #play button
                if playButton.isOver(pos):
                    print('click on start')
                #exit button
                if exitButton.isOver(pos):
                    print('click on exit')
            #hover over
            if event.type == pygame.MOUSEMOTION:
                #play button
                if playButton.isOver(pos):
                    playButton.color = (255,0,0)
                    print('the button is now red')
                else:
                    playButton.color = (0,255,0)
                #exit button
                if exitButton.isOver(pos):
                    exitButton.color = (255,0,0)
                    print('the button is now red')
                else:
                    exitButton.color = (0,0,255)
        
buttons()
