import pygame
import os
from pygame import font
from pygame.locals import *
import sys
# pygame.init()
# width_screen = 800
# height_screen = 448
# screen = pygame.display.set_mode((width_screen, height_screen))


pygame.font.init()
text_font = pygame.font.SysFont(None, 40)
white = (255, 255, 255)
black = (0, 0, 0)

def message_to_screen(msg, color, screen):
    screen_text = text_font.render(msg, 1, color)
    screen.blit(screen_text, (350, 224))

def Game_Control(screen):
    Paused = True
    while Paused:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_p]:
                    print(p)
                    Paused = False

        screen.fill(white)
        message_to_screen(msg = "Paused", color = black, screen = screen)


# while True:
#     keys = pygame.key.get_pressed()
#     for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_p:
#                     screen.fill(white)
#                     message_to_screen(msg = "Paused", color = black, screen = screen)
    
#     pygame.display.update()