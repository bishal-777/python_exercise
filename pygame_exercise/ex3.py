#optimized ex2 code by using dictionary and added captions
import pygame
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((600,400))

CYAN=(0,255,255)
MAGENTA=(255,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)

background=CYAN

key_dict={
    K_k:BLACK,
    K_r:RED,
    K_w:WHITE,
    K_b:BLUE,
    K_g:GREEN,
    K_c:CYAN,
    K_m:MAGENTA
}

running=True
while running==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        screen.fill(background)
        pygame.display.update()
        if event.type==KEYDOWN:
            if event.key in key_dict:
                background=key_dict[event.key]    

                caption="Background Color"+str(background)
                pygame.display.set_caption(caption)


pygame.quit() 