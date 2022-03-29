import pygame

pygame.init()
GRAY = (127, 127, 127)
screen = pygame.display.set_mode((640, 240))
screen.fill(GRAY)
BLACK = (0, 0, 0)
WHITE = (247, 247, 247)
ORANGE = (245, 126, 7)
running = True
while running:
    for event in pygame.event.get():
        if event.type == 256:
            running = False
    pygame.draw.ellipse(screen, WHITE, (110, 20, 80, 50))
    pygame.draw.ellipse(screen, WHITE, (70, 50, 160, 100))
    pygame.draw.ellipse(screen, WHITE, (30, 90, 260, 200))
    pygame.draw.ellipse(screen, BLACK, (130, 30, 8, 8))  
    pygame.draw.ellipse(screen, BLACK, (160, 30, 8, 8)) 
    pygame.draw.rect(screen, ORANGE, (145, 40, 40, 5))
    pygame.draw.ellipse(screen, BLACK, (130, 50, 5, 5))  
    pygame.draw.ellipse(screen, BLACK, (170, 50, 5, 5))
    pygame.draw.ellipse(screen, BLACK, (140, 55, 5, 5))  
    pygame.draw.ellipse(screen, BLACK, (160, 55, 5, 5))
    pygame.draw.ellipse(screen, BLACK, (150, 60, 5, 5))  
    pygame.display.update()  

pygame.quit()

        
