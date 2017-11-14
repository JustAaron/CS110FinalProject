##import invader
##import tower
##import path
##import castle
##import spawnpoint
import pygame
from pygame.locals import *

class Controller:
    def __init__(self):
        pygame.init()

        #Creates the window and title
        self.mainscreen = pygame.display.set_mode((1000,1000))
        pygame.display.set_caption("Tower Defense")
        
        self.clock = pygame.time.Clock()
        #Create background
        self.mainscreen.fill((255,255,188))
    
        #Event loop
        alive = True
        while alive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    alive = False
            pygame.display.update()


    pygame.quit()

def main():
    control = Controller()

main()




                                              
