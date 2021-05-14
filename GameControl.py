import pygame
import os
from pygame import font
from pygame.locals import *
import sys


pygame.font.init()
text_font = pygame.font.SysFont(None, 40)
white = (255, 255, 255)
black = (0, 0, 0)

def message_to_screen(msg, color, screen):
    screen_text = text_font.render(msg, 1, color)
    screen.blit(screen_text, (350, 224))


