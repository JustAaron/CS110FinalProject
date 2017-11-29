import pygame
import bullet
import math
#import path
#import time

class Tower:
    """Class represents the towers that protects the castle by killling invaders"""
    def __init__(self,img_file = "tower.png",rate=2,radius=5,price=100):
        """Initializes variables for the tower"""
        #Initializing variables
        self.cost = price
        self.level = 1
        self.rate = rate
        self.timer = 0
        self.radius = radius * 50
        #Creates image and rect
        self.image = pygame.image.load('assets/' + img_file).convert_alpha()
        self.rect = self.image.get_rect()
    
    '''def createicon(self,screen,mouse, bg):
        towerimg= self.image
        screen.blit(bg, self.rect, self.rect)
        towerRect = towerimg.get_rect()
        towerRect.center = (mouse)
        screen.blit(towerimg,towerRect.center)
    '''
    def place_tower(self, pathObj):
        #self.rect = pygame.mouse.get_pos()
        pos = pygame.mouse.get_pos()
        for i in range(len(pathObj.paths)):
            for j in range(len(pathObj.paths[i])):
                if(pathObj.paths[i][j] == 0 and pos[0] / 50 <= i + 1 and pos[0] / 50 >= i and pos[1] / 50 <= j + 1 and pos[1] / 50 >= j):
                    pathObj.paths[i][j] = -2

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
    










        
        
