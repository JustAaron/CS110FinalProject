import pygame, sys
from pygame.locals import *
import path

class Invader(pygame.sprite.Sprite):
    """Class represents the slimes that appear each wave"""
    def __init__(self,img_file,spawningpoint):
        """
            Descr: __init__ sets initial variables and image
            Params: self
                    img_file is a string containing file name
                    spawningpoint is a tuple containing coordinates
            Returns: none """
        
        pygame.sprite.Sprite.__init__(self)
        
        #Puts image into the invader
        image = pygame.image.load('assets/' + img_file).convert_alpha()
        self.image = pygame.transform.scale(image,(20,20))
        #Maintains reference to rectangle/allows movement
        self.rect = self.image.get_rect()
        self.rect.x = spawningpoint[0]
        self.rect.y = spawningpoint[1]
        #Stats of the Invaders
        self.health = 100
        self.speed = 30
        self.location = 1
        self.p = path.Path()
        
    def path(self):
        """
        Descr: path is a list of coordinates of the path
        Params: none
        Returns: string containing direction """
        
        if (self.rect[1] == 80) and (10 <= self.rect[0] <=140):
            return "right"
        elif (self.rect[0] == 170) and (80 <= self.rect[1] <= 290):
            return "down"
        elif (self.rect[1] == 320) and (170 <= self.rect[0] <= 290):
            return "right"
        elif (self.rect[0] == 320) and (120 <= self.rect[1] <= 320):
            return "up"
        elif (self.rect[1] == 110) and (310 <= self.rect[0] <= 650):
            return "right"

    def move(self, direction):
        """
        Descr: move changes rect based on direction given
        Params: self
                direction is a string containing direction
        Returns: none """
        
        self.direction = direction
        if self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed

    def healthbar(self,screen):
        """
        Descr: healthbar shows the health of the invader
        Params: self
                screen is a pygame object
        Returns: none """
        
        self.outline = pygame.draw.rect(screen,(0,0,0),(self.rect.x,self.rect.y-10,21,6),1)
        self.redbar = pygame.draw.rect(screen,(255,0,0),(self.rect.x,self.rect.y-10,self.health/5,5))
    


        


