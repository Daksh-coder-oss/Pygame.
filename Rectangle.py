import pygame

pygame.init()
rect1=pygame.display.set_mode((600,500))
work=False
while not work:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
pygame.draw.rect(rect1,(0,150,260),pygame.Rect(40,40,70,70))
pygame.display.flip()
