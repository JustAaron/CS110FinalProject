#import invader
import tower
##import path
##import castle
##import spawnpoint
import pygame, sys
from pygame.locals import *

class Controller:
    def __init__(self,width=700,height=650):
        pygame.init() #Calls the init
        self.width = width
        self.height = height
        
        #Creates the window and title
        self.mainscreen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Tower Defense")
        self.background = pygame.Surface(self.mainscreen.get_size()).convert()
        self.clock = pygame.time.Clock()
        
        #Starting Variables: Initial starting values recieved at beginning of game
        self.money = 500
        self.health = 20
        self.tower = []
        self.invader = []
        self.bullets = []
        self.towericon = False
        
        #Fonts
        self.largefont = pygame.font.SysFont('arial',40)
        self.font = pygame.font.SysFont('arial',15)
        """Image/Text and rect"""
        #Start
        self.start = pygame.draw.rect(self.mainscreen,(255,255,255),(260,245,180,100))
        #Tower
        self.towerimg = pygame.image.load('assets/' + "tower.png").convert()
        self.towerRect = self.towerimg.get_rect()
    
    def startMenu(self):
        #Create background, and text on background
        pygame.mouse.set_visible(True)
        #Background
        self.menuscreen = pygame.image.load('assets/' + "frontpage.png").convert()
        self.menuscreen = pygame.transform.scale(self.menuscreen,(self.width,self.height))
        self.mainscreen.blit(self.menuscreen,(0,0))


    def interface(self):
        #Area of variables
        self.mainscreen.fill((255,255,255))
        pygame.draw.rect(self.mainscreen,(0,0,0),(0,self.height-150,self.width,150),0)
        pygame.draw.line(self.mainscreen,(255,255,255),(200,self.height-150),(200,self.height),2)
        pygame.draw.line(self.mainscreen,(255,255,255),(500,self.height-150),(500,self.height),1)
        #Title of each box
        texttower = self.font.render("Towers",True, (255,255,255))
        self.mainscreen.blit(texttower,(90,515))
        #To see variables on screen
        self.towerRect.center = (40,550)
        self.mainscreen.blit(self.towerimg,self.towerRect)
        #Money
        moneytext = self.font.render("Money: "+ str(self.money),True, (255,255,255))
        self.mainscreen.blit(moneytext,(self.width-150,530))
        #Health
        healthtext = self.font.render("Health: "+ str(self.health),True, (255,255,255))
        self.mainscreen.blit(healthtext,(self.width-150,550))
    def gameLost(self):
        endmenu = pygame.image.load('assets/' + "endpage.png").convert()
        self.endmenu = pygame.transform.scale(self.endmenu,(self.width,self.height))
        self.mainscreen.blit(self.endmenu,(0,0))
    def mainLoop(self):
        #Creates the main game loop
        self.startMenu() #Creates the menu
        alive = True #Run loop
        while alive:
            #Creating main loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    alive = False
                if event.type == MOUSEBUTTONDOWN:
                    #Start
                    if self.start.collidepoint(pygame.mouse.get_pos()):
                        self.interface()
                    #To get Tower
                    elif self.towerRect.collidepoint(pygame.mouse.get_pos()):
                        if (self.money >= tower.Tower("tower.png").cost):
                            self.tower.append(tower.Tower("tower.png"))
                            self.money -= tower.Tower("tower.png").cost
                            new_tower = self.tower[-1]
                            self.towericon = True
                        self.interface()
                elif event.type == MOUSEMOTION:
                    if self.towericon:
                        new_tower.createicon(self.mainscreen,pygame.mouse.get_pos())
                elif event.type == MOUSEBUTTONUP:
                    if self.towericon:
                        self.towericon = False
        
            self.clock.tick(60)
            pygame.display.flip()
        if self.health == 0:
            self.gameLost()
        pygame.quit()

def main():
    main_window = Controller()
    main_window.mainLoop()

main()





                                              
