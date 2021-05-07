import pygame
import sys
import math
import os
from pygame.locals import *

pygame.init()

surface = pygame.display.set_mode((800, 448))
pygame.display.set_caption('Mario')

map_image = pygame.image.load(os.path.join("img", "map1.png"))
h = map_image.get_height()
w = map_image.get_width()
# map_image = pygame.transform.scale(map_image, (w, h*2))

# print(h)
FPS = 60
fpsClock = pygame.time.Clock()
class Map:
    bgX = 0
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

    winning_door = [(6530, 320, 30, 60)]


    def __init__(self):
        pass
    def drawMap(self):
        surface.blit(map_image, (self.bgX, 0))
        pygame.display.update()
    def drawBlock(self):
        for i in self.block:
            pygame.draw.rect(map_image, (255, 0, 0), i)

m = Map()
# for i in m.winning_door:
#     pygame.draw.rect(map_image, (255, 0, 0), i)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     m.drawMap()
#     bgX -= 8
#     if bgX < map_image.get_width() * -1:
#         bgX = map_image.get_width()

#     pygame.display.update()
#     fpsClock.tick(FPS)


    