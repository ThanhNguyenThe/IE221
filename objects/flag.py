import pygame
import sys
import math
import os
from pygame.locals import *

class Flag:
    hitBox = (6349, 67, 6, 290)
    def __init__(self, window):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("img", "flag.png")), (40, 32))
        self.rect = self.image.get_rect()
        self.rect.y = 317
        self.rect.x = 6352
        self.change_y = 0
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def update(self, player, bg, window):
        hitBox = pygame.Rect(self.hitBox)
        player_hitBox = pygame.Rect((abs(bg.bgX) + player.x, player.y, 32, 32))
        if hitBox.colliderect(player_hitBox):
            #move flag
            pass
        window.blit(self.image, (self.rect.x, self.rect.y))
    