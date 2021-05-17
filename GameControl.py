import pygame
import os
from pygame import font
from pygame.locals import *
import sys
import time

pygame.font.init()
pygame.mixer.init()

# pause_sound =  pygame.mixer.Sound(os.path.join('music', 'alaba.mp3'))

text_font = pygame.font.SysFont(None, 40)

white = (255, 255, 255)
black = (0, 0, 0)
pause_sound = pygame.mixer.Sound('music/alaba.wav')
def pause_Sound():
    pause_sound.play()
def message_to_screen(msg, color, screen, pos):
    screen_text = text_font.render(msg, 1, color)
    screen.blit(screen_text, pos)


def win_game(bg, player):
        hitBox = pygame.Rect(abs(bg.bgX) + player.x, player.y, 32, 32)
        winning_door = pygame.Rect(bg.winning_door)
        if hitBox[0] >= winning_door[0] + winning_door[2] and hitBox[1] + 32 < winning_door[1]:
            if hitBox[0] <= winning_door[0] + winning_door[2] and hitBox[1] + 32 < winning_door[1]:
                bg.time_collide -= 1
                if bg.time_collide < 0:
                    bg.time_collide = 0
        if bg.time_collide == 0:
            if hitBox.colliderect(winning_door):
                return True
        return False

def lose_game(player, enemy, window, bg):
    if player.dead(enemy, window, bg):
        return True
    return False