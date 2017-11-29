import pygame
import bullet
import math
#import time

class Tower(pygame.sprite.Sprite):
    """Class represents the towers that protects the castle by killling invaders"""
    
    def __init__(self, mouse, img_file = "tower.png", rate=2,radius=5,price=100):   
    	#initialize all the Sprite functionality
    	pygame.sprite.Sprite.__init__(self)
    	
    	self.cost = price
    	self.lever = 1
    	self.rate = rate
    	self.timer = 0
    	self.radius = radius
    	#create images and rec
    	self.image = pygame.image.load('assets/' + img_file).convert_alpha()
    	self.rect = self.image.get_rect()
    	#move ability
    	self.ablemove = False
    	self.rect.x = mouse[0]
    	self.rect.y = mouse[1]
    	
    def followmouse(self, change ):
    	self.rect.x += change[0]
    	self.rect.y += change[1]
    	
    def place_tower(self, pathObj):
    	#self.rect = pygame.mouse.get_pos()
    	pos = pygame.mouse.get_pos()
    	for i in range(len(pathObj.paths)):
    		for j in range(len(pathObj.paths[i])):
    			if(pathObj.paths[i][j] == 0 and pos[0] / 50 <= i + 1 and pos[0] / 50 >= i and pos[1] / 50 <= j + 1 and pos[1] / 50 >= j):
    				pathObj.paths[i][j] = -2
    				self.rect.x = i * 50
    				self.rect.y = j * 50
    				
    	#def place_tower(self):
    	
    	
    def upgrade(self,playermoney,cost,img_file):
    	if (playermoney > self.towercost):
    		playermoney -= cost
    		self.level += 1
    		self.damage += 15
    		self.speed += 1
    		self.radius += 2
    		self.range = (math.pi)(radius)**2
    		self.image = pygame.image.load('assets/' + img_file).convert_alpha()
    		self.rect = self.image.get_rect()
    	else:
    		return "Unable to upgrade: Money is not enough"
    		
    def target(self,enemy):
    	bullets = []
    	distanceToEnemy = sqrt((enemy.rect.x - self.rect.x)**2 + (enemy.rect.y - self.rect.y)**2)
    	if (distanceToEnemy < self.radius):
    		bullets.append(bullet.Bullet(self.rect.x, self.rect.y, (enemy.rect.x, enemy.rect.y), self.damage, "bullet.png", math.sin(((enemypos[0]-self.rect.x)**2)/distanceToEnemy)))
    		
    def get_info(self):
    	self.info = ""
    	line1 = "Tower: " + str(self.name) + "  Tower Level: " + str(self.level)
    	self.info.append(line1)
    	line2 = "Damage: " + str(self.damage) + "  Range: " + str(self.radius)
    	self.info.append(line2)
    	line3 = "Attack speed: " + str(self.speed)
    	self.info.append(line3)
    	return self.info









        
        
