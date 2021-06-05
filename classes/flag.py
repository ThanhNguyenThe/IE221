import pygame
import sys
import math
import os
from pygame.locals import *

class Flag:
    #tọa độ của flag
    """
    Cờ
        Attributes:
            hitBox: tuple
            score: list
        Methods:
            update(player, screen, bg): vẽ và update vị trí của flag
    """
    hitBox = (6349, 67, 6, 290)
    score = [0]
    def __init__(self):
        """khởi tạo flag"""
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("img", "flag.png")), (40, 32))
        self.rect = self.image.get_rect()
        self.y = 317
        self.x = 6352
        self.change_y = 0
    
    def update(self, player, screen, bg):
        """ vẽ và update vị trí của flag"""
        screen.blit(self.image, (self.x + bg.bgX, self.y))
        hitBox = pygame.Rect(self.hitBox)
        player_hitBox = pygame.Rect((abs(bg.bgX) + player.x, player.y, 32, 32))
        if hitBox.colliderect(player_hitBox): #nếu player chạm cột flag sẽ di chuyển
            self.score.append(player.y)
            while self.y >= player.y:
                self.y -= 0.5
    