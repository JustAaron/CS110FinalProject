import pygame, sys
from pygame.locals import *

class Invader(pygame.sprite.Sprite):
    """Class represents the slimes that appear each wave"""
    def __init__(self,spawningpoint,img_file):
        """Creates invader and initial positions"""
        pygame.sprite.Sprite.__init__(self)
        
        #Puts image into the invader
        self.image = pygame.image.load('assets/' + img_file).convert_alpha()
        
        #Maintains reference to rectangle/allows movement
        self.rect = self.image.get_rect()
        self.rect.x = spawningpoint[0]
        self.rect.y = spawningpoint[1]
        #Stats of the Invaders
        self.health = 100
        self.speed = 10

    def move_to_castle(self,screen):
        """Called each frame and moves self.speed pixels"""
        if self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "up":
            self.rect.y += self.speed
        elif self.direction == "down":
            self.rect.y += self.speed
        else:
            screen.blit(self.image,(self.rect))
            
    def update(self):
        screen.blit(self.image,(self.rect))
        #Hook: adds functionality which will be called






