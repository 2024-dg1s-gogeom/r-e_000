import pygame
from pygame.locals import *
from map import show_map

def front_render(font, maze, display_surf):
    display_surf.fill((0, 0, 0))
    title = font.render("Tap SPACE BAR to Start", True, (255, 255, 255))
    display_surf.blit(title, (210, 272))
    pygame.display.flip()

def play_render(font, maze, display_surf):
    display_surf.fill((0, 0, 0))
    pygame.draw.line(display_surf, (255, 255, 255), (400,0), (400,600), 2)
    pygame.draw.line(display_surf, (255, 255, 255), (0,300), (800,300), 2)  
    show_map(display_surf)
    pygame.display.flip()

def finish_render(font, maze, display_surf):
    display_surf.fill((0, 0, 0))
    ending = font.render("You WON !!", True, (255, 255, 255))
    display_surf.blit(ending, (370, 232))
    goingback = font.render("Tap ESC to return to start")
    display_surf.blit(goingback, (345, 282))


