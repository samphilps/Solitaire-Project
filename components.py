import pygame
class Screen():
    SCREENCOLOR = (76, 194, 115)
    SCREENWIDTH = 800
    SCREENHEIGHT = 620
    SCREENSIZE = (SCREENWIDTH,SCREENHEIGHT)
    FPS = 24
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREENSIZE)
    