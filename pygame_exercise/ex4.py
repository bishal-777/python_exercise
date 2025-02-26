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

font=pygame.font.SysFont(None,24)
img1=font.render('Hello World',True,BLUE)
img2=font.render('My first text display in pygame',True,RED)

background=CYAN

running=True
show_text1=False
show_text2=False
while running==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                show_text1=True
            if event.key==pygame.K_x:
                show_text2=True

    screen.fill(background)

    if show_text1:
        screen.blit(img1,(20,20))
    if show_text2:
        screen.blit(img2,(20,40))
    pygame.display.update()

pygame.quit()
