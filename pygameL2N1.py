
import pygame
from pygame.locals import *

pygame.init()
GRAY = (127, 127, 127)
screen = pygame.display.set_mode((640, 240))
screen.fill(GRAY)
BLACK = (0, 0, 0)
WHITE = (247, 247, 247)
ORANGE = (245, 126, 7)
ALICEBLUE = (240, 248, 255)
LIMEGREEN = (50, 205, 50)
MAGENTA = (255, 0, 255)
ROYALBLUE = (65, 105, 225)
img = pygame.image.load('Creeper.png')
img = pygame.transform.scale(img, (60, 80))
img.convert()
rect = img.get_rect()
rect.center = 320, 120



font1 = pygame.font.SysFont(None, 24)
up = font1.render('UP', True, BLACK)
font2 = pygame.font.SysFont(None, 24)
down = font2.render('DOWN', True, WHITE)
font3 = pygame.font.SysFont(None, 24)
left = font3.render('LEFT', True, LIMEGREEN)
font4 = pygame.font.SysFont(None, 24)
right = font4.render('RIGHT', True, ORANGE)

rect1 = pygame.Rect(290, 10, 60, 30)
rect2 = pygame.Rect(290, 200, 60, 30)
rect3 = pygame.Rect(10, 90, 60, 30)
rect4 = pygame.Rect(570, 90, 60, 30)
clear = pygame.Rect(0, 0, 640, 240)
move_left = (-10, 0)
move_right = (10, 0)
move_up = (0, -10)
move_down = (0,10)




pygame.draw.rect(screen, ALICEBLUE, rect1)
pygame.draw.rect(screen, ORANGE, rect2)
pygame.draw.rect(screen, ROYALBLUE, rect3)
pygame.draw.rect(screen, MAGENTA, rect4)
screen.blit(img, rect)
pygame.draw.rect(screen, LIMEGREEN, rect, 1)
screen.blit(up, (310, 10))
screen.blit(down, (294, 200))
screen.blit(left, (20, 90))
screen.blit(right, (574, 90))
pygame.display.update()

transparent = (0, 0, 0, 0)
moving = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == 256:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect1.collidepoint(event.pos):
                rect.move_ip(move_up)
                clear.move_ip(move_up)
                screen.fill(GRAY, clear)
                screen.blit(img, rect)
                pygame.draw.rect(screen, ALICEBLUE, rect1)
                pygame.draw.rect(screen, ORANGE, rect2)
                pygame.draw.rect(screen, ROYALBLUE, rect3)
                pygame.draw.rect(screen, MAGENTA, rect4)
                screen.blit(up, (310, 10))
                screen.blit(down, (294, 200))
                screen.blit(left, (20, 90))
                screen.blit(right, (574, 90))
                
                pygame.display.flip()

            elif rect2.collidepoint(event.pos):
                rect.move_ip(move_down)
                clear.move_ip(move_down)
                screen.fill(GRAY, clear)
                screen.blit(img, rect)
                pygame.draw.rect(screen, ALICEBLUE, rect1)
                pygame.draw.rect(screen, ORANGE, rect2)
                pygame.draw.rect(screen, ROYALBLUE, rect3)
                pygame.draw.rect(screen, MAGENTA, rect4)
                screen.blit(up, (310, 10))
                screen.blit(down, (294, 200))
                screen.blit(left, (20, 90))
                screen.blit(right, (574, 90))
                
                pygame.display.flip()

            elif rect3.collidepoint(event.pos):
                rect.move_ip(move_left)
                clear.move_ip(move_left)
                screen.fill(GRAY, clear)
                screen.blit(img, rect)
                pygame.draw.rect(screen, ALICEBLUE, rect1)
                pygame.draw.rect(screen, ORANGE, rect2)
                pygame.draw.rect(screen, ROYALBLUE, rect3)
                pygame.draw.rect(screen, MAGENTA, rect4)
                screen.blit(up, (310, 10))
                screen.blit(down, (294, 200))
                screen.blit(left, (20, 90))
                screen.blit(right, (574, 90))
                
                pygame.display.flip()

            elif rect4.collidepoint(event.pos):
                rect.move_ip(move_right)
                clear.move_ip(move_right)
                screen.fill(GRAY, clear)
                screen.blit(img, rect)
                pygame.draw.rect(screen, ALICEBLUE, rect1)
                pygame.draw.rect(screen, ORANGE, rect2)
                pygame.draw.rect(screen, ROYALBLUE, rect3)
                pygame.draw.rect(screen, MAGENTA, rect4)
                screen.blit(up, (310, 10))
                screen.blit(down, (294, 200))
                screen.blit(left, (20, 90))
                screen.blit(right, (574, 90))
                
                pygame.display.flip()






pygame.quit()