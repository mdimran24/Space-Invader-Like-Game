import pygame
import sys
import random
pygame.init()

Width = 800
Height = 600
Red = (255,0,0)
Blue = (0,0,255)
playersize = 50
pos = [(Width/2),(Height-2*playersize)]

enemysize = 50
enemypos = [random.randint(0,Width-enemysize), 0]
screen = pygame.display.set_mode((Width, Height))
enemyspeed = 0.35
game_over = False

def detect_collision(pos,enemypos):
    p_x = pos[0]
    p_y = pos[1]

    e_x = enemypos[0]
    e_y = enemypos[1]

    if (e_x >= p_x and e_x < (p_x + playersize)) or (p_x >= e_x and p_x < (e_x+enemysize)):
        
        if (e_y >= p_y and e_y < (p_y + playersize)) or (p_y >= e_y and p_y < (e_y+enemysize)):
            return True
    return False
    
while not game_over:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()


    if event.type == pygame.KEYDOWN:

        x = pos[0]
        y = pos[1]

        if event.key == pygame.K_LEFT:
            x -= 0.25
        elif event.key == pygame.K_RIGHT:
            x += 0.25

        pos = [x,y]

    screen.fill((0,0,0))
    if enemypos[1] >= 0 and enemypos[1] < Height:
        enemypos[1] += enemyspeed
    else:
        enemypos[0] = random.randint(0, Width-enemysize)
        enemypos[1] = 0

    if detect_collision(pos,enemypos):
        game_over = True
    pygame.draw.rect(screen, (Blue), (enemypos[0], enemypos[1], enemysize, enemysize))
    pygame.draw.rect(screen, (Red), (pos[0], pos[1], playersize, playersize))



    pygame.display.update()
