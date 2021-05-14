import pygame
import sys
import math
import os
from pygame.locals import *
from objects.Mario import *
from objects.mushroom import *
from Map import *
from GameControl import *
pygame.init()

width_screen = 800
height_screen = 448
width = 32
height = 32
FPS = 80
screen = pygame.display.set_mode((width_screen, height_screen))
pygame.display .set_caption('Mario')
bg = Map()
player = Mario(0, 100, 32, 32)
mushroom = Mushroom(0, 352, 32, 32)
flag = Flag(map_image)
run = True
bg.bgX = -5900

pause = False

while run:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if keys[pygame.K_p]: #pause
                pause = True
                screen.fill((255, 255, 255))
                message_to_screen('paused', black, screen)
            if keys[pygame.K_c]: #continue
                pause = False
    if bg.win(player, screen):
        message_to_screen('You win', white, screen)           
    if not pause and not bg.win(player, screen):
        bg.drawMap()
        bg.scrollBg(player)
        bg.gold_collect(player) 

        player.draw_hit_box(screen)
        player.move(bg)
        player.draw(screen)

        mushroom.draw_hit_box(screen)
        mushroom.draw(screen)
        mushroom.update()

        flag.update(player, bg, screen)
    fpsClock.tick(FPS)
    pygame.display.update()