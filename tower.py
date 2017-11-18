import pygame
import bullet
import math
#import time

class Tower:
    """Class represents the towers that protects the castle by killling invaders"""
    def __init__(self,img_file,name,rate,radius,price):
        """Initializes variables for the tower"""
        #Initializing variables
        self.cost = price
        self.level = 1
        self.name = name
        self.rate = rate
        self.timer = 0
        self.radius = radius
        self.range = (math.pi)(radius)**2
        #Creates image and rect
        self.image = pygame.image.load('assets/' + img_file).convert_alpha())
        self.rect = self.image.get_rect()
    
    def place_tower(self):
        position = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def upgrade(self,playermoney,self.towercost,img_file):
        if (playermoney > self.towercost):
            playermoney -= self.towercost
            self.level += 1
            self.damage += 15
            self.speed += 1
            self.radius += 2
            self.range = (math.pi)(radius)**2
            self.image = pygame.image.load('assets/' + img_file).convert_alpha())
            self.rect = self.image.get_rect()
        else:
            return "Unable to upgrade: Money is not enough"

    def target(self,enemeies):
        bullets = []
        if (sqrt((enemies.rect.x - self.rect.x)**2 + (enemies.rect.y - self.rect.y)**2)) < self.radius:
            bullets.append(bullet.Bullet())

    def get_info(self):
        self.info = ""
        line1 = "Tower: " + str(self.name) + "  Tower Level: " + str(self.level)
        self.info.append(line1)
        line2 = "Damage: " + str(self.damage) + "  Range: " + str(self.radius)
        self.info.append(line2)
        line3 = "Attack speed: " + str(self.speed)
        self.info.append(line3)
        return self.info










        
        
