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
        # make a sprites Group
        self.sprites = pygame.sprite.Group(tuple(self.tower)) # add invaders 
        
        #Fonts
        self.largefont = pygame.font.SysFont('arial',40,True)
        self.font = pygame.font.SysFont('arial',30,True)
        """Image/Text and rect"""
        #Start button
        self.start = pygame.draw.rect(self.mainscreen,(255,255,255),(260,245,180,100))
        #Tower
        self.towerimg = pygame.image.load('assets/' + "tower.png").convert()
        self.towerRect = self.towerimg.get_rect()
    
    def startMenu(self):
        #Create background, and text on background
        pygame.mouse.set_visible(True)
        #Background of start menu
        menuscreen = pygame.image.load('assets/' + "frontpage.png").convert()
        menuscreen = pygame.transform.scale(menuscreen,(self.width,self.height))
        self.mainscreen.blit(menuscreen,(0,0))


    def interface(self):
        # Make background of interface 
        mapscreen = pygame.image.load("assets/" + "mapscreen.png").convert()
        self.mainscreen.blit(mapscreen,(0,0))
        
        #To see variables on screen
        self.towerRect.center = (40,550)
        self.mainscreen.blit(self.towerimg,self.towerRect)
        
        #Money
        moneytext = self.font.render(str(self.money),True, (255,255,255))
        self.mainscreen.blit(moneytext,(175,510))
        #Health
        healthtext = self.font.render(str(self.health),True, (255,255,255))
        self.mainscreen.blit(healthtext,(175,585))
    
    
    def instruction_Menu(self):
    	# Make background of instruction menu
    	instructionima = pygame.image.load('assets/' + "instruction.png").convert()
    	self.mainscreen.blit(instructionima,(0,0))
    	
    	
    def gameLost(self):
    	# Make background of gamelost 
        endmenu = pygame.image.load('assets/' + "endpage.png").convert()
        self.endmenu = pygame.transform.scale(self.endmenu,(self.width,self.height))
        self.mainscreen.blit(self.endmenu,(0,0))
        
        
        	
    def instructionMenuScr(self):	
        while self.instruction_Menu_Scr:
        	self.instruction_Menu() #Creates the instruction menu screen
        	pygame.display.flip()
        	
    def gamemapScr(self):	
        while self.gamemap_Scr:
        	self.interface() #Creates the game menu screen
        	
        	for event in pygame.event.get():
        		if event.type == pygame.QUIT:
        			return pygame.quit()
        	pygame.display.flip()
    
    
    def startMenuScr(self):   
        while self.start_Menu_Scr:
        	self.startMenu() #Creates the start menu screen
        	
        	for event in pygame.event.get():
        		if event.type == pygame.QUIT:
        			return pygame.quit()
        			
        		if event.type == MOUSEBUTTONDOWN:
        			# Click start button
        			if self.start.collidepoint(pygame.mouse.get_pos()):
        				return self.gamemapScr()
        				
        			#if self.????.collidepoint(pygame.mouse.get_pos()):
        				#self.instruction_Menu_Scr = True
        				#self.start_Menu_Scr = False
        	pygame.display.flip()
        	
        	'''   
                    #To get Tower
                    elif self.towerRect.collidepoint(pygame.mouse.get_pos()):
                        if (self.money >= tower.Tower("tower.png",pygame.mouse.get_pos()).cost):
                            self.tower.append(tower.Tower("tower.png", pygame.mouse.get_pos()))
                            self.sprites.add(self.tower)
                            self.money -= tower.Tower("tower.png",pygame.mouse.get_pos()).cost
                            self.towericon = True
                elif event.type == MOUSEMOTION:
                	# draw the pictures when tower moving with mouse
                    if self.towericon:
                    	self.sprites.update()
                    	self.interface() # cover old tower image
                    	self.sprites.draw(self.mainscreen)  # draw new tower image
                elif event.type == MOUSEBUTTONUP:
                    if self.towericon:
                        self.towericon = False
        if self.health == 0:
            self.gameLost()'''
    def mainLoop(self):
        #Creates the main game loop
        
        # set different menu loop
        self.start_Menu_Scr = True
        self.instruction_Menu_Scr =True
        self.gamemap_Scr = True
        self.endpage_Scr = False
        self.winpage_Scr = False 
        
        self.startMenuScr()
        pygame.quit()

def main():
    main_window = Controller()
    main_window.mainLoop()

main()




                                              
