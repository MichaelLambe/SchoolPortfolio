
from rect import *
c = (100, 80, 50, 80)
v = (100, 50, 60, 80)
rect1 = Rect(v)
rect2 = Rect(c)
n = [randint(1,4),randint(1,4)]
m = [randint(1,4),randint(1,4)]
FPS = 30
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
       
    rect1.move_ip(n)
    rect2.move_ip(m)
    if rect1.left < 0:
        n[0] *= -1
    if rect1.right > width:
        n[0] *= -1
    if rect1.top < 0:
        n[1] *= -1
    if rect1.bottom > height:
        n[1] *= -1      
    
    if rect2.left < 0:
        m[0] *= -1
    if rect2.right > width:
        m[0] *= -1
    if rect2.top < 0:
        m[1] *= -1
    if rect2.bottom > height:
        m[1] *= -1      
    
    

    screen.fill(GRAY)
    pygame.draw.rect(screen, GREEN, rect1)
    pygame.draw.rect(screen, RED, rect2)
    if rect1.colliderect(rect2):
        pygame.draw.rect(screen, BLACK, rect1)
        pygame.draw.rect(screen, BLUE, rect2)
    clock.tick(FPS)
    pygame.display.flip()
    pygame.display.update()
    

pygame.quit()