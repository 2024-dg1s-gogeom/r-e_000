import pygame
from pygame.locals import *
from maze.maze import Maze
import render
def show_map(display_surf):
    drawList = [[200,150], [600,150], [200,450], [600,450]]
    gray = (200, 200, 200)
    black= (0, 0, 0)
    white= (255, 255, 255)
    for a,b in drawList:
        #Background cell
        pygame.draw.rect(display_surf, black, (a-200, b-150, 400, 300))

        #Frame
        pygame.draw.rect(display_surf, white, (a-162, b-102, 324, 204))
        
        #cross line
        pygame.draw.line(display_surf, white, (400,0), (400,600), 2)
        pygame.draw.line(display_surf, white, (0,300), (800,300), 2)

        #side polygon
        pygame.draw.polygon(display_surf, black, [[a+110, b+60], [a+160, b+100], [a-160, b+100], [a-110, b+60]])
        pygame.draw.polygon(display_surf, black, [[a+110, b-60], [a+160, b-100], [a-160, b-100], [a-110, b-60]])
        pygame.draw.polygon(display_surf, black, [[a+110, b+60], [a+160, b+100], [a+160, b-100], [a+110, b-60]])
        pygame.draw.polygon(display_surf, black, [[a-110, b+60], [a-160, b+100], [a-160, b-100], [a+110, b-60]])
        
        #side line
        pygame.draw.line(display_surf, white, [a+110, b+60], [a+160, b+100], 2)
        pygame.draw.line(display_surf, white, [a+110, b-60], [a+160, b-100], 2)
        pygame.draw.line(display_surf, white, [a-110, b+60], [a-160, b+100], 2)
        pygame.draw.line(display_surf, white, [a-110, b-60], [a-160, b-100], 2)

        #Central Frame
        pygame.draw.rect(display_surf, white, (a-110, b-60, 220, 120))

        #Cetral rectangle
        pygame.draw.rect(display_surf, black, (a-106, b-58, 212, 116))

    #pos information
    pygame.draw.rect(display_surf, white, (310, 250, 180, 100))
    pygame.draw.rect(display_surf, black, (312, 252, 176, 96))
    font=pygame.font.Font(None, 40)
    text=font.render("POSTION", True, white)
    display_surf.blit(text, (335, 255))

    #Coordinate
    i=-1
    center=[[200, 150, 0], [600, 150, 2], [200, 450, 4], [600, 450, 6]]
    pos_List=[[-10, -10], [-10, -145], [-150, -10], [120,-10], [-10, -90], [-10, 70]]
    con=["XP", "XN", "YP", "YN", "ZP", "ZN", "WP", "WN"]
    for p_x, p_y, in pos_List:
        i+=1
        for ps_x, ps_y, N in center:
            font=pygame.font.Font(None, 30)
            text=font.render(con[N+i], True, white)
            display_surf.blit(text, (ps_x+p_x, ps_y+p_y))
        if i==1:
            dis=(con[0], con[1])
            con.remove(con[0])
            con.remove(con[0])
            con.extend(dis)
            i=0
    pygame.display.flip()  