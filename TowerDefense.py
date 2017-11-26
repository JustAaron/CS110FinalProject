#import invader
import tower
##import path
##import castle
##import spawnpoint
import pygame, sys
from pygame.locals import *

class Controller:
    def __init__(self,width=600,height=600):
        pygame.init()
        self.width = width
        self.height = height
        
        #Creates the window and title
        self.mainscreen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Tower Defense")
        self.background = pygame.Surface(self.mainscreen.get_size()).convert()
        self.clock = pygame.time.Clock()
        
        #Create background, and text on background
        self.mainscreen.fill((255,255,255))
        largefont = pygame.font.SysFont('Comicsansms',50)
        text = largefont.render("Tower Defense", True, (0,0,0))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        textpos.centery = self.background.get_rect().centery - 250
        self.mainscreen.blit(text,textpos)
        pygame.mouse.set_visible(True)
        
        #Starting Variables: Initial starting values recieved at beginning of game
        self.money = 500
        self.health = 20
        self.tower = []
        self.invader = []
        self.bullets = []

    def interface(self):
        self.mainscreen.fill((255,255,255))
        self.mainscreen.fill((255,255,255))
        #To see variables on screen
        self.mainscreen.fill((255,255,255))
        self.font = pygame.font.SysFont('arial',15)
        #Money
        moneytext = self.font.render("Money: "+ str(self.money),True, (0,0,0))
        self.mainscreen.blit(moneytext,(500,450))
        #Health
        healthtext = self.font.render("Health: "+ str(self.health),True, (0,0,0))
        self.mainscreen.blit(healthtext,(500,460))
            
    def mainLoop(self):
        #Creates the main game loop
        alive = True #Run loop
        
        while alive:
            self.interface()
            #Creating icons
            towerimg= pygame.image.load('assets/' + "tower.png").convert()
            towerRect = towerimg.get_rect()
            towerRect.center = (525,100)
            self.mainscreen.blit(towerimg,towerRect)
            towericon = False
            #Creating main loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    alive = False
                if event.type == MOUSEBUTTONDOWN:
                    #To get Towers
                    xpos = event.pos[0]
                    ypos = event.pos[0]
                    if towerRect.collidepoint(pygame.mouse.get_pos()):
                        if (self.money >= tower.Tower("tower.png").cost):
                            #Adding tower to total list
                            self.tower.append(tower.Tower("tower.png"))
                            #Money is taken away due to price of Tower
                            self.money -= tower.Tower("tower.png").cost
                            #Tower is dragged away and placed
                            new_tower = self.tower[-1]
                            towericon = True
                        else:
                            mtext= self.font.render("Not enough money",True, (0,0,0))
                            self.mainscreen.blit(mtext,(500,490))
                            pygame.time.delay(40)
                elif event.type == MOUSEMOTION:
                    if towericon:
                        new_tower.createicon(self.mainscreen,pygame.mouse.get_pos())
                elif event.type == MOUSEBUTTONUP:
                    towericon = False         
        
            self.clock.tick(60)
            pygame.display.flip()
        pygame.quit()


def main():
    main_window = Controller()
    main_window.mainLoop()

main()




                                              
