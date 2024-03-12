import pygame 
import time

pygame.init()

window_surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Circle')

game_over = False

x1 = 400
y1 = 300
 
x1_change = 0       
y1_change = 0
 
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    window_surface.blit(mesg, [400, 300])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
            
    if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
        game_over = True
 
 
    x1 += x1_change
    y1 += y1_change
    window_surface.fill((255, 255, 255))
    pygame.draw.circle(window_surface, (255, 0, 0), (x1, y1), 25)
 
    pygame.display.update()
 
    clock.tick(30)
message("You lost", (255, 0, 0))
pygame.display.update()
time.sleep(2)
 
pygame.quit()
quit()