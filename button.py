import pygame 

class button():
    def __init__(self,screen,x,y,width,height):
	self.x = x
	self.y = y
	self.height = height
	self.width = width
	self.rect = pygame.draw.rect(screen,(0,0,0),(self.x,self.y,self.width,self.height))

