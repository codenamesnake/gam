import pygame
from sys import exit

pygame.init()

surface= pygame.display.set_mode((1920,1800)) #width , hight
pygame.display.set_caption('test001')
clock=pygame.time.Clock()
font=pygame.font.Font(None, 200)


surface_ground=pygame.Surface((3200,1800))
surface_color= pygame.Surface((3200,1400))

surface_color.fill('slateblue')


surface_ground.fill('forestgreen')


surface_back = pygame.image.load('/home/ashmith/Desktop/images/sun.png').convert() #converts into a form where pygame understands


kratos=pygame.image.load('/home/ashmith/Desktop/images/kra.jpeg').convert()
kratos_rect=kratos.get_rect(topleft =(875,920))




text_test=font.render('SON', True,'black')


skull=pygame.image.load('/home/ashmith/Desktop/images/skull.jpeg')
skull_rect=skull.get_rect(topleft = (200,920))


while True:

#dislays everythin in loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    surface.blit(surface_ground,(0,0))
    surface.blit(surface_color,(0,0))
    #top left is origin
    surface.blit(surface_back,(1600,100))


    
    kratos_rect.x -=7
    if kratos_rect.left <-400: kratos_rect.right=2250
    surface.blit(kratos,kratos_rect)


    surface.blit(text_test,(0,0))
    skull_rect.x -=5
    if skull_rect.left <-400: skull_rect.right=2250
    surface.blit(skull,skull_rect)

    pygame.display.update() #refresher and updater
    clock.tick(60)#how much fps
