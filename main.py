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
width = 32
height = 32
FPS = 80
screen = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption('Mario')
bg = Map()
player = Mario(0, 100, 32, 32)


run = True
bg.bgX = 0
for i in bg.gold_point:
    pygame.draw.rect(map_image , (0, 255, 0), i, width = 2)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    bg.drawMap()
    bg.drawBlock()
    bg.scrollBg(player)
    bg.gold_collect(player)
    player.draw_hit_box(screen)
    player.move(bg)
    player.draw(screen)
    bg.win(player)
    fpsClock.tick(FPS)
    pygame.display.update()