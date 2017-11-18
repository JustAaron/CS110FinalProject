import pygame, sys
from pygame.locals import *

class Invader(pygame.sprite.Sprite):
    """Class represents the slimes that appear each wave"""
    def __init__(self,spawningpoint,castle,img_file):
        """Creates invader and initial positions"""
        pygame.sprite.Sprite.__init__(self)
        
        #Puts image into the invader
        self.image = pygame.image.load('assets/' + img_file).convert_alpha()
        
        #Maintains reference to rectangle/allows movement
        self.rect = self.image.get_rect()
        self.rect.x = spawningpoint[0]
        self.rect.y = spawningpoint[1]
        self.endx = castle[0]
        self.endy = castle[1]
        #Stats of the Invaders
        self.health = 100
        self.speed = 5
    
    def path_one(self):
        if self.rect.x <= 200 and self.rect.y == spawningpoint[1]:
            self.direction = "right"
        elif self.rect.x == 205 and self.rect.y <= 250:
            self.direction = "down"
        elif self.rect.x <= 405 and self.rect.y == 255:
            self.direction = "right"
        elif self.rect.x == 405 and self.rect.y <= 420:
            self.direction = "down"
        elif self.rect.x <= 470 and self.rect.y == 425:
            self.direction = "right"
        elif self.rect.x == 475 and self.rect.y >= (castle[0]-5):
            self.direction = "up"
        elif self.rect.x <= (castle[0]-5) and self.rect.y == castle[0]:
            self.direction = "right"

    def move_to_castle(self):
        """Called each frame and moves a pixel"""
        if self.direction == "right":
            self.rect.x += self.speed
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "up":
            self.rect.y += self.speed
        if self.direction == "down":
            self.rect.y += self.speed
    def update(self):
        #Hook: adds functionality which will be called






