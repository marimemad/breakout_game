import pygame
from Baddel import *
from Configurations import *
from Ball import *
from Bricks import *
import time


pygame.init()

screen=pygame.display.set_mode((screenwidth,screenheigth))
pygame.display.set_caption('Breakout') 

font = pygame.font.Font('freesansbold.ttf', 20)

clock = pygame.time.Clock()
baddel=Baddel(screen)
ball=Ball(screen)

bricks=[]
y=50

for row in range (4):
    for col in range(12):
        
        brick=Bricks(screen,( (brickwidth+5)*col)+8,y)
        bricks.append(brick)
        
    y+=brickheight+5


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    
    clock.tick(70)
    screen.blit(back_ground, (0, 0))
    baddel.draw()
    ball.draw()
    
    #hit baddel
    if ball.hit_object(baddel):
        ball.y_direction*=-1
    
    for brick in bricks:
        brick.draw()
        
        #hit brick
        if ball.hit_object(brick):
            bricks.remove(brick)
            ball.y_direction*=-1
            
    # if win
    if not bricks and hearts!=0:
        font = pygame.font.Font('freesansbold.ttf', 50)
        win=font.render('Win', True, green)
        screen.blit(win,(350,250))
        del ball
        pygame.display.update()
        time.sleep(3)
        quit()
            
            
    if not(ball.hit_object(baddel)) and baddel_y <= ball.y <= screenheigth:
        hearts-=1
        if hearts==0:
            font = pygame.font.Font('freesansbold.ttf', 50)
            game_over=font.render('Game Over', True, red)
            screen.blit(game_over,(250,250))
            del ball
            pygame.display.update()
            time.sleep(3)
            quit()
            
        else:    
            del ball
            ball=Ball(screen)

    
    text = font.render('Hearts = '+str(hearts), True, white) 
    screen.blit(text,(650,10))
    pygame.display.update()
    
