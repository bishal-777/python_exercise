#This program changes background color as per user input key
import pygame

pygame.init()

screen=pygame.display.set_mode((400,400))

CYAN=(0,255,255)
MAGENTA=(255,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)

background=CYAN

running=True
while running==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        screen.fill(background)
        pygame.display.update()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_m:
                background=MAGENTA

            elif event.key==pygame.K_r:
                background=RED
            
            elif event.key==pygame.K_g:
                background=GREEN


pygame.quit()