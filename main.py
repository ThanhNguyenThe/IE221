import pygame
import sys
import math
import os
from pygame.locals import *
from objects.Mario import *
from Map import *

pygame.init()

width_screen = 800
height_screen = 448
width = 16
height = 16
FPS = 80
screen = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption('Mario')
bg = Map()
player = Mario(0, 100, 32, 32)


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    bg.drawMap()
    bg.bgX = -5000
    player.draw_hit_box(screen)
    player.move(bg)
    player.draw(screen)

    if bg.bgX < map_image.get_width() * -1:
        bg.bgX = map_image.get_width()
    pygame.display.update()
    fpsClock.tick(FPS)