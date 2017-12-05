import pygame
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):
    """Class creates bullet"""
    def __init__(self,pos):
        """
        Descr: Function creates bullet and initial positions
        Params: pos: tuple containing coordinates of invader
        Returns: none """
        
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)
        #Creating image and rect
        self.image = pygame.image.load('assets/' + "bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect()
        #Initial position
        self.rect.x = pos[0]
        self.rect.y = pos[1]

            
    def to_invader(self,enemypos):
        """
        Descr:Function moves bullet to position of invader
        Params: enemypos: tuple containing invader position
        Returns: none """
        
        self.rect.x = enemypos[0]
        self.rect.y = enemypos[1]




    


