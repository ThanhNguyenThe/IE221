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
screen = pygame.display.set_mode([width_screen, height_screen])
pygame.display .set_caption('Mario')
bg = Map()
player = Mario(0, 100, 32, 32)
mushroom = Mushroom(0, 352, 32, 32)
flag = Flag(bg.map_image)
run = True
bg.bgX = 0
fpsClock = pygame.time.Clock()
pause = False
game_stop = False


while run:
<<<<<<< HEAD

=======
    start_time = pygame.time.get_ticks()
>>>>>>> 3e28b4cf7d487862ed17ff8560d37beb1981c7c9
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if keys[pygame.K_p]: #pause
                pause = True
                screen.fill((255, 255, 255))
                message_to_screen('paused', black, screen, (300, 224))
                message_to_screen('press c to continue', black, screen, (250, 260))
                pause_sound.play()
            if keys[pygame.K_c]: #continue
                pause = False 



<<<<<<< HEAD
    if not pause and not win_game(bg, player, screen) and not lose_game(player, mushroom, screen, bg):
        bg.drawMap(screen)
=======
    if not pause and not win_game(bg, player) and not lose_game(player, mushroom, screen, bg):

        bg.drawMap()
>>>>>>> 3e28b4cf7d487862ed17ff8560d37beb1981c7c9
        bg.scrollBg(player)
        bg.gold_collect(player) 

        player.draw_hit_box(screen)
        player.move(bg)
        player.draw(screen)


        mushroom.draw_hit_box(screen, bg)
        mushroom.draw(screen, bg)
        mushroom.update()
        
<<<<<<< HEAD
        flag.update(player, screen, bg)

=======
        flag.update(player, bg, screen)
        out='Time: {time:03d}'.format(time = start_time // 1000)
        message_to_screen(out, white, screen, (600, 10))
>>>>>>> 3e28b4cf7d487862ed17ff8560d37beb1981c7c9
    fpsClock.tick(FPS)

    

    pygame.display.update()
    