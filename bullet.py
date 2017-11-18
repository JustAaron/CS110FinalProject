import pygame

from pygame.locals import *

class Bullet(pygame.sprite.Sprite):
    def __int__(self,x,y,speed,enemypos,damage,img_file):
        """Class creates bullet""" #enemypos is tuple with x and y
        #Initializing variables in the bullet class
        self.x = x
        self.y = y
        self.damage = damage
        self.speed = speed
        self.angle = math.sin((enemypos[0]-self.rect.x)**2)/dist)
        
        #Creating image and rect
        self.image = pygame.image.load('assets/' + img_file).convert_alpha())
        self.rect = self.image.get_rect()
            
    def to_invader(self):
        """Moving position to enemy position"""
        #Finds distance to invader
        dist = ((enemypos[0]-self.rect.x)**2)+((enemypos[1]-self.rect.y)**2)**0.5
        if (dist != 0):
            self.x -= enemypos[0]*self.speed
            self.y -= enemypos[1]*self.speed
                


    


