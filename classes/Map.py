import pygame
import sys
import math
import os
from pygame.locals import *
from classes.flag import *
from game.GameControl import *
pygame.init()

# surface = pygame.display.set_mode((800, 448))
# pygame.display.set_caption('Mario')


# map_image = pygame.transform.scale(map_image, (w, h*2))

# print(h)
# FPS = 60
# fpsClock = pygame.time.Clock()
class Map:
    """Background Map"""
    map_image = pygame.image.load(os.path.join("img", "map1.png"))
    bgX = 0 #tọa độ x của map
    time_collide = 100 #số lần nhảy qua của player nên đổi tên khác :(
    block = [
    (0, 384, 2206, 64), #ground
    (2270, 384, 480, 64),
    (2850, 384, 2040, 64),
    (4960, 384, 3020, 64),

    (512, 256, 30, 30), #block
    (640, 256, 162, 30),
    (2463, 256, 98, 30),
    (3007, 256, 34, 30),
    (3200, 256, 30, 30),
    (3390, 256, 30, 30),
    (3392, 256, 30, 30),
    (3488, 256, 30, 30),
    (3584, 256, 30, 30),
    (3774, 256, 35, 30),
    (4126, 256, 70, 30),
    (5374, 256, 128, 30),
    (6336, 352, 30, 30),

    (705, 129, 30, 30), #up_block 732 156
    (2560, 129, 256, 30),
    (2910, 129, 130, 30),
    (3486, 129, 30, 30),
    (3870, 129, 100, 30),
    (4094, 129, 126, 30),

    (1474, 256, 60, 128), #plum
    (1824, 256, 62, 128),
    (1214, 284, 64, 98),
    (894, 316, 64, 66),
    (5214, 316, 62, 66),
    (5728, 316, 60, 66),

    (4288, 352, 30, 30), #stair
    (4320, 320, 30, 62),
    (4352, 286, 30, 94),
    (4384, 254, 30, 126),

    (4478, 254, 30, 126),
    (4510, 286, 30, 94),
    (4542, 320, 30, 62),
    (4574, 350, 30, 30),

    (4736, 350, 30, 30),
    (4768, 320, 30, 62),
    (4800, 286, 30, 94),
    (4832, 254, 60, 126),
    
    (4960, 254, 30, 126),
    (4992, 286, 30, 94),
    (5024, 320, 30, 60),
    (5056, 350, 30, 30),

    (5792, 350, 30, 30),
    (5824, 320, 30, 62),
    (5856, 286, 30, 94),
    (5885, 254, 30, 126),
    (5920, 222, 30, 160),
    (5952, 190, 30, 190),
    (5984, 158, 30, 222),
    (6016, 126, 60, 256),
    ]

    gold_point = [
        (512, 258, 30, 32),
        (675, 258, 30, 32),
        (735, 258, 30, 32),
        (2498, 258, 30, 32),
        (705, 131, 30, 32),
        (3010, 131, 30, 32),
        (3392, 258, 30, 32),
        (3488, 258, 30, 32),
        (3584, 258, 30, 32),
        (3486, 131, 30, 32),
        (4128, 131, 30, 32),
        (4160, 131, 30, 32),
        (5441, 258, 30, 32)
    ]
    winning_door = (6530, 320, 30, 60)   

    def __init__(self):
        pass
    def drawMap(self, screen):
        """vẽ map từ tọa độ abs(bgX)"""
        screen.blit(self.map_image, (self.bgX, 0))
        
    def drawBlock(self): 
        """vẽ hitbox các block"""
        for i in self.block:
            pygame.draw.rect(self.map_image, (255, 0, 0), i)

    def scrollBg(self, player): 
        """trượt background"""
        key = pygame.key.get_pressed()
        if player.x > 300 and key[pygame.K_RIGHT]:
            self.bgX -= 5
        elif player.x < 100 and key[pygame.K_LEFT]:
            self.bgX += 5
        if self.bgX <= -5950: #-5950
            self.bgX = -5950
        if self.bgX >= 0:
            self.bgX = 0

    def gold_collect(self, player):
        """render tiền khi chạm block vàng"""
        gold_image = pygame.transform.scale(pygame.image.load(os.path.join('img', 'gold.png')), (30, 30)) #load ảnh
        hitBox = pygame.Rect(abs(self.bgX) + player.x, player.y, 32, 32)
        for i in self.gold_point:
            i = pygame.Rect(i)
            if i.colliderect(hitBox):
                self.map_image.blit(gold_image, (i[0], i[1] - 40, 30, 30)) #mario chạm vào ô hitbox (hơi bị đẩy xuống) hiện tiền
                coin_sound.play()
        pass
    
    



    