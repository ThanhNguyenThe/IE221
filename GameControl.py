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
coin_sound = pygame.mixer.Sound('music/coin.wav')
mariodie_sound = pygame.mixer.Sound('music/mariodie.wav')

time_start = pygame.time.get_ticks()

def message_to_screen(msg, color, screen, pos):
    screen_text = text_font.render(msg, 1, color)
    screen.blit(screen_text, pos)

def score():
    pass
def win_game(bg, player, screen):
        hitBox = pygame.Rect(abs(bg.bgX) + player.x, player.y, 32, 32)
        winning_door = pygame.Rect(bg.winning_door)
        if hitBox[0] >= winning_door[0] + winning_door[2] and hitBox[1] + 32 < winning_door[1]:
            if hitBox[0] <= winning_door[0] + winning_door[2] and hitBox[1] + 32 < winning_door[1]:
                bg.time_collide -= 1
                if bg.time_collide < 0:
                    bg.time_collide = 0
        if bg.time_collide == 0:
            if hitBox.colliderect(winning_door):
                message_to_screen('You win', white, screen, (300, 224))
                return True
        return False

def lose_game(player, enemy, window, bg):
    if player.dead(enemy, window, bg):
        mariodie_sound.play()
        message_to_screen('You lose', white, window, (300, 224))
        return True
    return False

def time_counter(screen, pause):
    game_time = round(pygame.time.get_ticks() / 1000)
    game_time = str(game_time)
    message_to_screen('time:'+ game_time, black, screen, (400, 10))