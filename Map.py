import pygame
import sys
import math
from pygame.locals import *

pygame.init()

surface = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Mario')

map_image = pygame.image.load('IE221/map.png')
h = map_image.get_height()
bgX = 0
FPS = 60
fpsClock = pygame.time.Clock()
class Map:
    ground = [(0, 190, 1103, h),
    (1135, 190, 1375, h),
    (1425, 190, 2445, h),
    (2480, 190, 3990, h),
    ]

    block = [(255, 126, 270, 141),
    (319, 126, 400, 141),
    (1230, 126, 1279, 141),
    (1503, 126, 1520, 141),
    (1600, 126, 1615, 141),
    (1695, 126, 1710, 141),
    (17433, 126, 1758, 141),
    (1790, 126, 1805, 141),
    (1885, 126, 1900, 141),
    (2063, 126, 2093, 141),
    (2687, 126, 2750, 141),
    ]

    up_block = [(352, 62, 367, 80),
    (1279, 62, 1407, 80),
    (1455, 62, 1520, 80),
    (1743, 62, 1758, 80),
    (1935, 62, 1985, 80),
    (2047, 62, 2110, 80),
    ]

    plum = [(190, 737, 127, 191),
    (912, 737, 943, 191),
    (607, 142, 639, 190),
    (447, 158, 479, 190),
    (2607, 158, 2638, 190),
    (2864, 158, 2894, 190)
    ]

    stair = [
        (2143, 175, 2207, 190),
        (2159, 160, 2207, 190),
        (2175, 143, 2207, 190),
        (2191, 127, 2207, 190),

        (2239, 127, 2303, 190),
        (2255, 143, 2303, 190),
        (2271, 160, 2303, 190),
        (2287, 175, 2303, 190),

        (2368, 175, 2448, 190),
        (2384, 160, 2448, 190),
        (2400, 143, 2448, 190),
        (2416, 127, 2448, 190),
        
        (2480, 127, 2544, 190),
        (2496, 143, 2544, 190),
        (2512, 160, 2544, 190),
        (2528, 175, 2544, 190),

        (2894, 175, 3038, 190),
        (2910, 160, 3038, 190),
        (2926, 143, 3038, 190),
        (2942, 127, 3038, 190),
        (2958, 111, 3038, 190),
        (2974, 95, 3038, 190),
        (2990, 79, 3038, 190),
        (3006, 63, 3038, 190),
    ]

    winning_door = (3265, 160, 3280, 190)

    
    def __init__(self):
        pass
    def drawMap(self):
        surface.blit(map_image, (bgX, 0))
        pygame.display.update()
    def drawBlock(self):
        for i in self.block:
            pygame.draw.rect(surface, (255, 0, 0), i)

m = Map()   
m.drawBlock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    m.drawMap()
    bgX -= 2
    if bgX < map_image.get_width() * -1:
        bgX = map_image.get_width()
    

    pygame.display.update()
    fpsClock.tick(FPS)


    