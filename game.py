import pygame
from sys import exit

pygame.init()

surface= pygame.display.set_mode((1920,1800)) #width , hight
pygame.display.set_caption('test001')
clock=pygame.time.Clock()
while True:

#dislays everythin in loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update() #refresher and updater
    clock.tick(30)#how much fps
