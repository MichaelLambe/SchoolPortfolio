from cmath import rect
import pygame
from pygame.locals import *

PURPLE = (89, 3, 133)
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((640, 240))

dir = {K_LEFT: (-5, 0),
K_RIGHT: (5, 0),
K_UP: (0, -5),
K_DOWN: (0, 5)}

dir2 = {K_a: (-5, 0),
K_d: (5, 0),
K_w: (0, -5),
K_s: (0, 5)}
 
start = (0, 0)
size = (0, 0)
drawing = False
running = True
rect_list = []

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            size = 0, 0
            drawing = True
            
        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            rect = pygame.Rect(start, size)
            rect_list.append(rect)
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
        
        if event.type == KEYDOWN:
            if event.key in dir:
                v = dir[event.key]
                rect_list[0].move_ip(v)
        
        if event.type == KEYDOWN:
            if event.key in dir2:
                b = dir2[event.key]
                rect_list[1].move_ip(b)

    screen.fill(GRAY)
    for rect in rect_list:
        pygame.draw.rect(screen, PURPLE, rect, 2)
    pygame.draw.rect(screen, BLACK, (start, size), 1 )
    pygame.display.update()

pygame.quit()