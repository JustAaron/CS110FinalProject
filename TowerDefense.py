##import invader
##import tower
##import path
##import castle
##import spawnpoint
import pygame, sys
from pygame.locals import *

class Controller:
    def __init__(self,width=600,height=800):
        pygame.init()
        self.width = width
        self.height = height
        #Creates the window and title
        self.mainscreen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Tower Defense")
        self.background = pygame.Surface(self.mainscreen.get_size()).convert()
        
        #Starting Variables: Money recieved to create tower initially
        
        
        self.enemies = []
        for i in range(): #FILL
            self.enemies.append() #FILL add enemies into the list
            self.sprites = pygame.sprite.Group() #FILL create sprite Group
        
    def mainLoop(self):
        alive = True
        while alive:
            #Create background, and text on background --- start menu can go below
            self.mainscreen.fill((255,255,188)) #image colored light yellow -- can be changed to an image
            font = pygame.font.SysFont('Courier',40,False,False)
            text = font.render("Tower Defense", True, (0,0,0))
            self.mainscreen.blit(text, [200,200])
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.quit() #Quit menu can go here
                    alive = False
                #######Include mouse click to get tower
                #######If position is clicked, money is lost and tower is created
        
            for i in range(len(self.enemies)):
                # When bullet collides with enemies destroy bullet
                if pygame.sprite.collide_rect(self.bullet,self.enemies[i]):
                    #bullet destroyed
                    self.enemies[i].health -= 5 #Fix so that it loses health for each collision
                    if self.enemies[i].health == 0: #enemies have no health
                        self.enemies[i].kill()
                        del self.enemies[i]
                #When enemies reach the castle
                elif pygame.sprite.collide_rect(self.enemies[i],castle.Castle):
                    self.enemies[i].kill()
                    del self.enemies[i]
                    
                break
            self.sprites.update()
            self.screen.blit(self.background, (0,0))
            
                
        
            
                                                  
            pygame.display.flip()
            

    pygame.quit()

def main():
    main_window = Controller()
    main_window.mainLoop()

main()
