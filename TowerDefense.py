#import invader
import tower
##import path
##import castle
##import spawnpoint
import pygame, sys
from pygame.locals import *

class Controller:
    def __init__(self,width=600,height=600):
        pygame.init() #Calls the init
        self.width = width
        self.height = height
        
        #Creates the window and title
        self.mainscreen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Tower Defense")
        self.background = pygame.Surface(self.mainscreen.get_size()).convert()
        self.gameimage = pygame.image.load("assets/frontpage.png") #fill in with map of game
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
        self.start = self.largefont.render("START", True, (75,0,188))
        self.startRect = self.start.get_rect()
        #Instructions
        self.instruct = self.largefont.render("INSTRUCTIONS", True, (75,0,188))
        self.instructRect = self.instruct.get_rect()
        #Tower
        self.towerimg = pygame.image.load('assets/' + "tower.png").convert()
        self.towerRect = self.towerimg.get_rect()
        

    def button(self,image,rect,center,color,position):
        pygame.draw.rect(self.mainscreen,color,position,0)
        rect.center = center
        self.mainscreen.blit(image,rect)
    
    def startMenu(self):
        #Create background, and text on background
        pygame.mouse.set_visible(True)
        #Background
        self.menuscreen = pygame.image.load('assets/' + "frontpage.png").convert()
        self.menuscreen = pygame.transform.scale(self.menuscreen,(600,600))
        self.menu = self.menuscreen.get_rect()
        self.mainscreen.blit(self.menuscreen,(0,0))
        #Title
        title = self.largefont.render("Tower Defense", True, (255,255,255))
        titlepos = title.get_rect()
        titlepos.centerx = self.background.get_rect().centerx
        titlepos.centery = self.background.get_rect().centery - 250
        self.mainscreen.blit(title,titlepos)
        #Buttons
        self.button(self.start,self.startRect,(200,500),(255,255,255),(150,477,100,40))
        self.button(self.instruct,self.instructRect,(400,500),(255,255,255),(280,477,240,40))

    def interface(self):
        #Area of variables
        self.mainscreen.fill((255,255,255))
        pygame.draw.rect(self.mainscreen,(0,0,0),(0,450,600,150),0)
        pygame.draw.line(self.mainscreen,(255,255,255),(200,450),(200,600),2)
        pygame.draw.line(self.mainscreen,(255,255,255),(500,450),(500,600),1)
        #Title of each box
        texttower = self.font.render("Towers",True, (0,0,0))
        self.mainscreen.blit(texttower,(520,470))
        #To see variables on screen
        self.towerRect.center = (40,500)
        self.mainscreen.blit(self.towerimg,self.towerRect)
        #Money
        moneytext = self.font.render("Money: "+ str(self.money),True, (255,255,255))
        self.mainscreen.blit(moneytext,(520,470))
        #Health
        healthtext = self.font.render("Health: "+ str(self.health),True, (255,255,255))
        self.mainscreen.blit(healthtext,(520,490))
    def mainLoop(self):
        #Creates the main game loop
        self.startMenu() #Creates the menu
        alive = True #Run loop
        self.towerSelected = False
        while alive:
            new_tower = tower.Tower()
            #Creating main loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    alive = False
                if event.type == MOUSEBUTTONDOWN:
                    #Start
                    if self.startRect.collidepoint(pygame.mouse.get_pos()):
                        self.interface()
                    #To get Tower
                    elif self.towerRect.collidepoint(pygame.mouse.get_pos()):
                        if (self.money >= new_tower.cost):
                            self.towerSelected = True
                            self.tower.append(new_tower)
                            self.money -= new_tower.cost
                            self.towericon = True
                        #self.interface()
                elif event.type == MOUSEMOTION:
                    if self.towericon:
                        self.createicon(new_tower, pygame.mouse.get_pos())
                elif event.type == MOUSEBUTTONUP:
                    if self.towericon:
                        self.towericon = False
        
            self.clock.tick(60)
            pygame.display.flip()
        pygame.quit()
    def createicon(self, tower, position):
        self.map = pygame.image.load("assets/map2.png")
        self.mainscreen.blit(self.map, (0,0))
        #self.mainscreen.blit(self.
        self.mainscreen.blit(tower.image, position)

def main():
    main_window = Controller()
    main_window.mainLoop()

main()
