import pygame
from Configurations import *


class Baddel():
    
    def __init__(self,surface):
        self.width=baddel_width
        self.height=baddel_height
        self.x=baddel_x
        self.y=baddel_y
        self.surface=surface
        
    def draw(self):
        self.update()
        pygame.draw.rect(self.surface, white,pygame.Rect( self.x ,self.y, self.width, self.height), 3)


    def update(self):
        pos = pygame.mouse.get_pos()
        self.x=pos[0]-50
        
        if self.x > screenwidth -self.width:
            self.x = screenwidth -self.width 
        
        if self.x<0:
            self.x=1
