import pygame
from Configurations import *


class Bricks():
    
    def __init__(self,surface,x,y):
        self.surface=surface
        self.x=x
        self.y=y
        self.width=brickwidth
        self.height=brickheight
        
    def draw(self):
       pygame.draw.rect(self.surface, pink,pygame.Rect(self.x,self.y, self.width, self.height))
       
       
    
    
