import pygame
import os
from pygame.locals import *
pygame.init()

# window = pygame.display.set_mode((500,500))
# pygame.display.set_caption("Mario")

width_screen = 600
height_screen = 224
width = 16
height = 16

walkRight = [pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run1.png")), (width, height)),
            pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run2.png")), (width, height)),
            pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run3.png")), (width, height))]

walkLeft = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run1.png")), (width, height)), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run2.png")), (width, height)), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run3.png")), (width, height)), True, False)]

deadImage = pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_die.png")), (width, height))
jumpImage = pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_jump.png")), (width, height))
char = pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_stand.png")), (width, height))
clock = pygame.time.Clock()

class Mario():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.isJump = False
        self.isLeft = False
        self.isRight = False
        self.horizonFacing = 'right'
        self.walkCount = 0 
        self.jumpCount = 10
        self.hitBox = (self.x, self.y, self.x + 32, self.y + 32)
        
    def draw(self, window):
        if self.walkCount + 1 >= 9:
            self.walkCount =  0
        if self.isLeft and self.isJump == False:
            window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.isRight and self.isJump == False:
            window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.isJump:
            if self.horizonFacing == 'right':
                window.blit(jumpImage, (self.x, self.y))
            else:
                window.blit(pygame.transform.flip(jumpImage, True, False), (self.x, self.y))
        else:
            if self.horizonFacing == 'right':
                window.blit(char, (self.x, self.y))
            else: 
                window.blit(pygame.transform.flip(char, True, False), (self.x, self.y))
        
    def draw_hit_box(self, window):
        hitBox = (self.x, self.y, 32, 32)
        pygame.draw.rect(window, [0, 255, 0], hitBox, 2) 
    
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
            self.isLeft = True
            self.horizonFacing = 'left'
            self.isRight = False
        elif keys[pygame.K_RIGHT] and self.x < width_screen - self.width - self.vel:
            self.x += self.vel
            self.isRight = True
            self.horizonFacing = 'right'
            self.isLeft = False
        else:
            self.isRight = False
            self.isLeft = False
            self.walkCount = 0

        if not(self.isJump):
            if keys[pygame.K_SPACE]:
                self.isJump = True
                self.isRight = False
                self.isLeft = False
                self.walkCount = 0
        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
    def Mario_interaction(self, bg):
        self.hitBox = (abs(bg.bgX) + self.x, self.y, abs(bg.bgX) + self.x + 32, self.y + 32)          
        for i in bg.block:
            if (self.hitBox[0] < i[0] + i[2] and
                self.hitBox[2] > i[0] and
                self.hitBox[1] < i[1] + i[3] and
                self.hitBox[3] > i[1]):
                print("true")


        # for i in block:
        #     if self.y in range(i[1], i[1] + i[3]):
        #         # right interaction
        #         if (self.x + 16) > i[0]:
        #             self.x = i[0]
        #         # left interaction
        #         elif (self.x < i[0] + i[2]):
        #             self.x = i[0] + i[2]
        #     elif self.x in range(i[0], i[0] + i[2]):
        #         # above
        #         if (self.y + 16) < i[1]:
        #             self.y = i[1]
        #         # under
        #         elif self.y < (i[1] + i[3]):
        #             self.y = i[1] + i[3]
        #     else: 
        #         pass
        pass


def gameWindow():
    window.fill([255,255,255])
    player.draw(window)
    # player.draw_hit_box(window)
    pygame.display.update()

# player = Mario(200, 410, 64, 64)
# run  = True

# while run:
#     clock.tick(60)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
        
#     player.move()
#     gameWindow()
# pygame.quit()
