import pygame
import sys
import math
import os
from pygame.locals import *

class Flag:
    hitBox = (6349, 67, 6, 290)
    score = [0]
    def __init__(self, map):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("img", "flag.png")), (40, 32))
        self.rect = self.image.get_rect()
        self.y = 317
        self.x = 6352
        self.change_y = 0
        map.blit(self.image, (self.x, self.y))
    
    def update(self, player, bg, map):
        map.blit(self.image, (self.x, self.y))
        hitBox = pygame.Rect(self.hitBox)
        player_hitBox = pygame.Rect((abs(bg.bgX) + player.x, player.y, 32, 32))
        if hitBox.colliderect(player_hitBox):
            self.score.append(player.y)
            for i in range(10):
                self.y -= 1
    