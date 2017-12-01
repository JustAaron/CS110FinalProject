import pygame, sys
from pygame.locals import *

class Invader(pygame.sprite.Sprite):
    """Class represents the slimes that appear each wave"""
    def __init__(self,img_file,spawningpoint):
        """Creates invader and initial positions"""
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
        
    def path(self):
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
        """Called each frame and moves self.speed pixels"""
        self.direction = direction
        if self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed
            
    def update(self):
        screen.blit(self.image,(self.rect))
        #Hook: adds functionality which will be called

    def getDirection(self, pathObj):
        startXY = pathObj.getPathXY(self.location)
        nextXY = pathObj.getPathXY(pathObj.getNextPath)
        if(startXY[i] == nextXY[i] and startXY[j] < nextXY[j]):
            return "down"
        elif(startXY[i] == nextXY[i] and startXY[j] > nextXY[j]):
            return "up"
        elif(startXY[i] < nextXY[i] and startXY[j] == nextXY[j]):
            return "right"
        elif(startXY[i] > nextXY[i] and startXY[j] == nextXY[j]):
            return "left"
        


