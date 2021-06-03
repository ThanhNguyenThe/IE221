import pygame
import os
from pygame import font
from pygame.event import Event
from pygame.locals import *
import sys
import time

pygame.font.init()
pygame.mixer.init()
pygame.init()

#file điều khiển các luồng trạng thái game

#set up âm thanh, màu , ...
text_font = pygame.font.SysFont(None, 40)
white = (255, 255, 255)
black = (0, 0, 0)

pause_sound = pygame.mixer.Sound('music/alaba.wav')
coin_sound = pygame.mixer.Sound('music/coin.wav')
mariodie_sound = pygame.mixer.Sound('music/mariodie.wav')

time_start = pygame.time.get_ticks()


def message_to_screen(msg, color, screen, pos): 
    """Render text."""
    screen_text = text_font.render(msg, 1, color)
    screen.blit(screen_text, pos)

def score():
    pass

def is_win_game(bg, player, screen):
        """Kiểm tra người chơi đã thắng chưa."""
        hitBox = pygame.Rect(abs(bg.bgX) + player.x, player.y, 32, 32)
        winning_door = pygame.Rect(bg.winning_door)
        #nếu nhân vật ở trong khoảng không trên cánh cổng thì -1 time collide
        if hitBox.left < winning_door.left and hitBox.right > winning_door.left and hitBox.bottom < winning_door.top:
            bg.time_collide -= 1
        if hitBox.right > winning_door.right and hitBox.left < winning_door.right and hitBox.bottom < winning_door.top:
            bg.time_collide -= 1
        if bg.time_collide < 0:
            bg.time_collide = 0
        if bg.time_collide == 0:
            if hitBox.colliderect(winning_door):
                return True
        return False

def win_game_screen(screen):
    """Màn hình khi thắng."""
    message_to_screen('You win', white, screen, (300, 224))

def is_lose_game(player, enemy, window, bg): #player chết thì thua
    """Kiểm tra người chơi đã thua chưa."""
    if player.dead(enemy, window, bg):
        return True
    return False

def lose_game_screen(screen): #màn hình lose
    """Màn hình khi thua."""
    mariodie_sound.play()
    message_to_screen('You lose', white, screen, (300, 224))

def infor_screen(screen, name): #màn hình nhập tên
    """Màn hình nhập tên người chơi."""
    screen.fill(white)
    message_to_screen('Enter your name:', black, screen, (300, 150))
    pygame.draw.rect(screen, black, (300, 200, 300, 100))
    message_to_screen(name, white, screen, (300, 205))
    message_to_screen('Press Enter to play game', black, screen, (300, 350))
    return name
    