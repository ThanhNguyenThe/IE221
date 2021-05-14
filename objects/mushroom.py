import pygame
import os
from pygame.locals import *
from objects.entitybase import EntityBase
pygame.init()

width = 32
height = 32
walk = [pygame.transform.scale(pygame.image.load(os.path.join("img", "mushroom1.png")), (width, height)),
        pygame.transform.scale(pygame.image.load(os.path.join("img", "mushroom2.png")), (width, height))]
die = pygame.transform.scale(pygame.image.load(os.path.join("img", "mushroom_die.png")), (width, height))

class Mushroom(EntityBase):

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel = 5
        self.isDie = False
        self.walkCount = 0
    
    def draw(self, window):
        if self.walkCount + 1 >= 4:
            self.walkCount = 0
        window.blit(walk[self.walkCount // 2], (self.x , self.y))
        self.walkCount += 1

    def draw_hit_box(self, window):
        hitBox = (self.x, self.y, 32, 32)
        pygame.draw.rect(window, [0, 0, 255], hitBox, 2) 
    
    def update(self):
        self.x += self.vel
        if self.x + 32  > 800 or self.x < 0:
            self.vel = - self.vel