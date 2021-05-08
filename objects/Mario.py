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
        self.vel_x = 3
        self.vel_y = 3
        self.isJump = False
        self.isLeft = False
        self.isRight = False
        self.horizonFacing = 'right'
        self.walkCount = 0 
        self.jumpCount = 10

        
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
    
    def move(self, bg):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > self.vel_x:
            self.x -= self.vel_x
            self.isLeft = True
            self.horizonFacing = 'left'
            self.isRight = False
        elif keys[pygame.K_RIGHT] and self.x < width_screen - self.width - self.vel_x:
            self.x += self.vel_x
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
            self.vel_y = -15
            if keys[pygame.K_SPACE] == False:
                self.isJump = False

        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
	        self.vel_y = 10

        self.y += self.vel_y
        if self.y > 448 : 
            self.y = 416
        
        #collision
        hitBox = pygame.Rect(abs(bg.bgX) + self.x, self.y, 32, 32)
        keys = pygame.key.get_pressed()   
        for i in bg.block:
            i = pygame.Rect(i[0], i[1], i[2], i[3])
            #x collision
            # if i.colliderect(hitBox[0], self.y , 32, 32):
            #     if hitBox[0] >= i[0]:
            #         self.vel_x = 0
            #y collision
            if i.colliderect(hitBox[0], self.y , 32, 32):
                if self.vel_y < 0:
                    self.y = i[1] + i[3]
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    self.y = i[1] - 32
                    self.vel_y = 0

            
                    


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
