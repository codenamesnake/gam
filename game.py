import pygame
from sys import exit

pygame.init()

surface= pygame.display.set_mode((1920,1800)) #width , hight
pygame.display.set_caption('test001')
clock=pygame.time.Clock()
font=pygame.font.Font(None, 200)

surface_color= pygame.Surface((1920,1800))
surface_color.fill('slateblue')
surface_back = pygame.image.load('/home/ashmith/Desktop/dice.png')
text_test=font.render('DICE', True,'Red')


while True:

#dislays everythin in loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    surface.blit(surface_color,(0,0)) #top left is origin
    surface.blit(surface_back,(700,600))
    surface.blit(text_test,(0,0))

    pygame.display.update() #refresher and updater
    clock.tick(60)#how much fps
