import pygame
from pygame.locals import *



pygame.init()
BLACK = (0, 0, 0)
WHITE = (247, 247, 247)
screen = pygame.display.set_mode((640, 240))
screen.fill(BLACK)

running = True
while running:
    for event in pygame.event.get():
        if event.type == 256:
            running = False

    pygame.draw.rect(screen, WHITE, (318, 10, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 20, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 30, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 40, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 50, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 60, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 70, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 80, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 90, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 100, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 110, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 120, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 130, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 140, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 150, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 160, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 170, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 180, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 190, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 200, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 210, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 220, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 230, 4, 4))
    pygame.draw.rect(screen, WHITE, (318, 240, 4, 4))
    pygame.draw.rect(screen, WHITE, (0, 2, 640, 4))
    pygame.draw.rect(screen, WHITE, (0, 234, 640, 4))
    pygame.draw.rect(screen, WHITE, (2, 80, 4, 26))
    pygame.draw.rect(screen, WHITE, (634, 40, 4, 26))
    pygame.draw.rect(screen, WHITE, (560, 140, 4, 4))
    myfont1 = pygame.font.SysFont("freesansbold.ttf", 42)
    label1 = myfont1.render(str(2), 1, (WHITE))
    screen.blit(label1, (280,10))
    myfont2 = pygame.font.SysFont("freesansbold.ttf", 42)
    label2 = myfont2.render(str(4), 1, (WHITE))
    screen.blit(label2, (340,10))

    pygame.display.update()  



pygame.quit()
