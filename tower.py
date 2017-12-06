import pygame
import math
#import time

class Tower(pygame.sprite.Sprite):
	"""Class represents the towers that protects the castle by killling invaders"""
		
	def __init__(self, mouse, img_file = "tower.png",radius=100,price=100):
		"""
		Descr: __init__ sets initial variables and image
		Params: mouse is a tuple containing coordinates
				img_file is a string containing image name
				radius and price is int
		Returns: none """
		#initialize all the Sprite functionality
		pygame.sprite.Sprite.__init__(self)

		self.cost = price
		self.level = 1
		self.radius = radius
		#create images and rec
		self.image = pygame.image.load('assets/' + img_file).convert_alpha()
		self.rect = self.image.get_rect()
		#move ability
		self.ablemove = False
		self.rect.x = mouse[0]
		self.rect.y = mouse[1]

	def followmouse(self, change):
		"""
		Descr: followmouse chnges rect based on change
		Params: change is a tuple containing new coordinates of change
		Returns: none """
		self.rect.x += change[0]
		self.rect.y += change[1]

	def inRange(self,enemyX,enemyY):
		"""
		Descr: inRange tells if enemy is in range of tower
		Params: enemyX/enemyY are int of the x and y coordinates
		Returns: Boolean Expression(True/False) if in/not in range """
		distanceToEnemy = math.sqrt((enemyX - self.rect.x)**2 + (enemyY - self.rect.y)**2)
		if (distanceToEnemy < self.radius):
			return True
		else:
			return False










        
        
