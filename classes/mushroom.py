import pygame
import os
from pygame.locals import *
pygame.init()

width = 32
height = 32
#load sprite
walk = [pygame.transform.scale(pygame.image.load(os.path.join("img", "mushroom1.png")), (width, height)),
        pygame.transform.scale(pygame.image.load(os.path.join("img", "mushroom2.png")), (width, height))]
die = pygame.transform.scale(pygame.image.load(os.path.join("img", "mushroom_die.png")), (width, height))

class Mushroom(pygame.sprite.Sprite):
    """Nấm"""
    def __init__(self, x, y, w, h):
        """Khởi tạo."""
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel = 2
        self.isDie = False
        self.walkCount = 0
    
    def draw(self, window, bg, xpos):
        """
        Vẽ và thay đổi sprite khi di chuyển.
        Di chuyển trong 1 khoảng x nhất định.
        """
        if self.isDie:
            window.blit(die, (self.x + bg.bgX, self.y))
        if self.walkCount + 1 >= 4:
            self.walkCount = 0
        window.blit(walk[self.walkCount // 2], (self.x + bg.bgX, self.y))
        self.walkCount += 1
        self.x += self.vel
        #vẽ và thay đổi sprite khi di chuyển
        #di chuyển trong 1 khoảng x nhất định
        if self.x + 32  > xpos[1] or self.x < xpos[0]:
            self.vel = - self.vel
        

    def draw_hit_box(self, window, bg):
        """Vẽ hitbox."""
        hitBox = (self.x + bg.bgX, self.y, 32, 32)
        pygame.draw.rect(window, [0, 0, 255], hitBox, 2) 


    def update(self, player, bg):
        """Văng khỏi map khi bị chết."""
        player_hitbox = pygame.Rect(player.x - bg.bgX, player.y, 32, 32)
        hitBox = pygame.Rect(self.x, self.y, 32, 32)
        if player_hitbox.colliderect(hitBox):
            if player_hitbox[1] + 32 >= hitBox.top and player_hitbox.top != hitBox.top:
                self.y = 800
    
