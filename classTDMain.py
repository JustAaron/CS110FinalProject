import pygame
from pygame.locals import *

class Controller:
    def __init__(self):
        #Creates the window
        pygame.init()
        self.mainscreen = pygame.display.set_mode((1000,1000))
        pygame.display.set_caption("Tower Defense")
        self.counter = 0 
        self.clock = pygame.time.Clock()
        self.clock.tick(30)
        #Event loop
        alive = True
        while alive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    alive = False

            pygame.display.update

    def incrementLabel(self):
        self.counter +=1
    pygame.quit()

def main():
    controls = Controller()

main()




                                              
