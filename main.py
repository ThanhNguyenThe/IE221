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
mushroom = Mushroom(10, 352, 32, 32)
mushroom1 = Mushroom(2270, 352, 32, 32)

flag = Flag(bg.map_image)

run = True
bg.bgX = -5000

fpsClock = pygame.time.Clock()
pause = False
game_stop = False
name_input = True
elaspsed_time = 0
start_time = pygame.time.get_ticks()

name = ''
while run:

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
            if event.type == pygame.KEYDOWN:
                name += event.unicode
            if keys[pygame.K_RETURN]:
                name_input = False
                start_time = 0
    if pause:
        start_time = pygame.time.get_ticks() - elaspsed_time
    if name_input:
        infor_screen(screen, name)

    if is_win_game(bg, player, screen):
        win_game_screen(screen)
    if is_lose_game(player, mushroom, screen, bg) or is_lose_game(player, mushroom1, screen, bg):
        lose_game_screen(screen)

    if not pause and not name_input and not is_win_game(bg, player, screen) and not is_lose_game(player, mushroom, screen, bg) and not is_lose_game(player, mushroom1, screen, bg):
        bg.drawMap(screen)
        bg.scrollBg(player)
        bg.gold_collect(player) 

        player.draw_hit_box(screen)
        player.move(bg)
        player.draw(screen)

        mushroom.draw_hit_box(screen, bg)
        mushroom.draw(screen, bg, (0, 800))
        mushroom.update(player, bg)
        mushroom1.draw_hit_box(screen, bg)
        mushroom1.draw(screen, bg, (2270, 2700))
        mushroom1.update(player, bg)
        
        flag.update(player, screen, bg)

        elaspsed_time = pygame.time.get_ticks() - start_time
        message_to_screen('time:' + str(int(elaspsed_time / 1000)) + 's', white, screen, (300, 10))
    fpsClock.tick(FPS)
    pygame.display.update()
    