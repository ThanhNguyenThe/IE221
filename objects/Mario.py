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
        self.hitBox = (self.x, self.y, 48, 48)
        
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
        self.hitBox = (self.x, self.y, 48, 48)
        pygame.draw.rect(window, [0, 255, 0], self.hitBox, 2) 
    
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
                self.y -= (self.jumpCount ** 2) * 0.1 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

    def Mario_interaction(self, block):
        for i in range(self.x, self.x + 48):
            for j in block: 
                if i in range(j[0], j[0] + j[2]): 
                    if self.y < j[1] + j[3]: #under block
                        self.y = j[1] + j[3]
                
                    if self.y < j[1]: #on block
                        self.y = j[1]
                    
                #side block
        pass

# def gameWindow():
#     window.fill([255,255,255])
#     player.draw(window)
#     # player.draw_hit_box(window)
#     pygame.display.update()

# player = Mario(200, 410, 64, 64)
# run  = True

# while run:
#     clock.tick(60)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
        
    # player.move()
    # gameWindow()
# pygame.quit()
