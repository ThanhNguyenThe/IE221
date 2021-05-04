import pygame
import sys
import math
import os
from pygame.locals import *

pygame.init()

surface = pygame.display.set_mode((600, 224))
pygame.display.set_caption('Mario')

map_image = pygame.image.load(os.path.join("img", "map.png"))

h = map_image.get_height()
# print(h)
bgX = 0
FPS = 60
fpsClock = pygame.time.Clock()
class Map:
    block = [(0, 190, 1103, h-190), #ground
    (1135, 190, 240, 34),
    (1425, 190, 1020, 34),
    (2480, 190, 1510, 34),

    (255, 126, 15, 15), #block
    (319, 126, 81, 15),
    (1230, 126, 49, 15),
    (1503, 126, 17, 15),
    (1600, 126, 15, 15),
    (1695, 126, 15, 15),
    (1743, 126, 15, 15),
    (1790, 126, 15, 15),
    (1885, 126, 15, 15),
    (2063, 126, 30, 15),
    (2687, 126, 63, 15),
    (3168, 175, 15, 15),

    (352, 62, 15, 18), #up_block
    (1279, 62, 128, 18),
    (1455, 62, 65, 18),
    (1743, 62, 15, 18),
    (1935, 62, 50, 18),
    (2047, 62, 63, 18),

    (737, 127, 30, 63), #plum
    (912, 127, 31, 63),
    (607, 142, 32, 48),
    (447, 158, 32, 32),
    (2607, 158, 31, 32),
    (2864, 158, 30, 32),

    (2143, 175, 64, 15), #stair
    (2159, 160, 48, 30),
    (2175, 143, 32, 47),
    (2191, 127, 16, 63),

    (2239, 127, 16, 63),
    (2255, 143, 16, 47),
    (2271, 160, 16, 30),
    (2287, 175, 16, 15),

    (2368, 175, 64, 15),
    (2384, 160, 64, 30),
    (2400, 143, 48, 47),
    (2416, 127, 32, 63),
    
    (2480, 127, 16, 63),
    (2496, 143, 16, 47),
    (2512, 160, 16, 30),
    (2528, 175, 16, 15),

    (2894, 175, 144, 15),
    (2910, 160, 128, 30),
    (2926, 143, 112, 47),
    (2942, 127, 96, 63),
    (2958, 111, 80, 79),
    (2974, 95, 64, 95),
    (2990, 79, 48, 111),
    (3006, 63, 32, 127),
    ]

    winning_door = (3265, 160, 15, 30)


    def __init__(self):
        pass
    def drawMap(self):
        surface.blit(map_image, (bgX, 0))
        pygame.display.update()
    def drawBlock(self):
        for i in self.block:
            pygame.draw.rect(map_image, (255, 0, 0), i)

m = Map()
# for i in m.block:
#     pygame.draw.rect(map_image, (255, 0, 0), i)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     m.drawMap()
#     bgX -= 3
#     if bgX < map_image.get_width() * -1:
#         bgX = map_image.get_width()

#     pygame.display.update()
#     fpsClock.tick(FPS)


    