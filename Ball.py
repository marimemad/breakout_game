import pygame
import random
from Configurations import *


class Ball():
    
    def __init__(self,surface):
        self.surface=surface
        self.radius = 20
        self.size=10
        self.x=400
        self.y=300
        self.x_direction=3
        self.y_direction=3
        
    def draw(self):
        self.update()
        pygame.draw.circle(self.surface, white, (self.x, self.y), self.size)
        
    def update(self):
        self.x += self.x_direction
        self.y += self.y_direction
 
            # Bounce the ball if needed
        if self.y > screenheigth - self.size or self.y < self.size:
            self.y_direction*= -1
        
        if self.x > screenwidth - self.size or self.x < self.size:
            self.x_direction *= -1
    
    def hit_object(self,obj):
        if  obj.x+obj.width+15 >= self.x+self.radius >=obj.x and obj.y <= self.y <= obj.y+obj.height:
            return(True)
        return(False)
    
    #def hit_floor(self):
        #if not( baddel_x + baddel_width +15 >= self.x+self.radius >= baddel_x and baddel_y <= self.y <= baddel_y+baddel_height):
             #if baddel_y <= self.y <= screenheigth:
                #print('wid')
            
    
        
                        
        
            
