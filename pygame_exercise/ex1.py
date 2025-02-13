#This program prints blank blue screen
import pygame

pygame.init()

screen=pygame.display.set_mode((640,240))

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        screen.fill(BLUE)
        pygame.display.update()

pygame.quit()
