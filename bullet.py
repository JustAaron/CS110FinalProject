import pygame
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):
    """Class creates bullet"""
    def __init__(self,pos):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)
        #Creating image and rect
        self.image = pygame.image.load('assets/' + "bullet.png").convert()
        self.image = pygame.transform.scale(self.image, (10,10))
        self.rect = self.image.get_rect()
        #Initial position
        self.rect.x = pos[0]
        self.rect.y = pos[1]

            
    def to_invader(self,enemypos):
        """Moving position to enemy position"""
        #Finds distance to invader
        dist = ((enemypos[0]-self.rect.x)**2)+((enemypos[1]-self.rect.y)**2)**0.5
        if (dist != 0):
            if enemypos[0] > self.rect.x:
                self.rect.x -= (enemypos[0] + 30)
            elif enemypos[0] < self.rect.x:
                self.rect.x += (enemypos[0] + 30)
            elif enemypos[1] > self.rect.x:
                self.rect.y -= (enemypos[1]+ 30)
            elif enemypos[1] < self.rect.x:
                self.rect.y += (enemypos[1]+ 30)




    


