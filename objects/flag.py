import pygame
import sys
import math
import os
from pygame.locals import *

class Flag:
    hitBox = (6349, 67, 6, 290)
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("img", "flag.png")), (40, 32))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.change_y = 0
    
    def move(self, y):
        self.change_y += y
    
    def update(self):
        self.rect.y -= self.change_y