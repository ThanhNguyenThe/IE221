import pygame
import sys
import math
import os
from pygame.locals import *
from objects.Mario import *
from Map import *

pygame.init()

width_screen = 600
height_screen = 224
width = 16
height = 16

surface = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption('Mario')
map = Map()
player = Mario(0, 190-16, 16, 16)


run = True 
map.drawBlock()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    player.move()
    map.drawMap()
    player.draw(surface)
    # player.Mario_interaction(map.block)
    bgX -= 3
    if bgX < map_image.get_width() * -1:
        bgX = map_image.get_width()

    pygame.display.update()
    fpsClock.tick(FPS)