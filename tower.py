import pygame
import math
#import time

class Tower(pygame.sprite.Sprite):
    """Class represents the towers that protects the castle by killling invaders"""
    
    def __init__(self, mouse, img_file = "tower.png",radius=100,price=100):
    	#initialize all the Sprite functionality
    	pygame.sprite.Sprite.__init__(self)
    	
    	self.cost = price
    	self.level = 1
    	self.radius = radius
    	#create images and rec
    	self.image = pygame.image.load('assets/' + img_file).convert()
    	self.rect = self.image.get_rect()
    	#move ability
    	self.ablemove = False
    	self.rect.x = mouse[0]
    	self.rect.y = mouse[1]
    	
    def followmouse(self, change):
    	self.rect.x += change[0]
    	self.rect.y += change[1]
    	
    def upgrade(self,playermoney,image,rect,img_file):
    	if (playermoney >= self.towercost):
    		playermoney -= cost
    		self.level += 1
    		self.radius += 50
    		self.range = (math.pi)(radius)**2
    		self.image = pygame.image.load('assets/' + img_file).convert_alpha()
    		self.rect.x = rect[0]
    		self.rect.y = rect[1]
    	else:
    		return "Unable to upgrade: Money is not enough"
    		
    def inRange(self,enemyX,enemyY):
    	distanceToEnemy = math.sqrt((enemyX - self.rect.x)**2 + (enemyY - self.rect.y)**2)
    	if (distanceToEnemy < self.radius):
    		return True
    		
    def get_info(self):
    	self.info = ""
    	line1 = "Tower: " + str(self.name) + "  Tower Level: " + str(self.level)
    	self.info.append(line1)
    	line2 = "Damage: " + str(self.damage) + "  Range: " + str(self.radius)
    	self.info.append(line2)
    	line3 = "Attack speed: " + str(self.speed)
    	self.info.append(line3)
    	return self.info









        
        
