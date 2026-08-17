import pygame

pygame.init()

surface= pygame.display.set_mode((1920,1800)) #width , hight

while True:

#dislays everythin in loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

pygame.display.update() #refresher and updater
