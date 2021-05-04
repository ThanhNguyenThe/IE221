import pygame
import os
from pygame.locals import *
pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Mario")

walkRight = [pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run1.png")), (48,48)),
            pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run2.png")), (48,48)),
            pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run3.png")), (48,48))]

walkLeft = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run1.png")), (48,48)), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run2.png")), (48,48)), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run3.png")), (48,48)), True, False)]

deadImage = pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_die.png")), (48,48))
jumpImage = pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_jump.png")), (48,48))
char = pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_stand.png")), (48,48))
clock = pygame.time.Clock()

class Mario():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
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
        elif keys[pygame.K_RIGHT] and self.x < 500 - self.width - self.vel:
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

    def Mario_interaction(sefl):
        pass

def gameWindow():
    window.fill([255,255,255])
    player.draw(window)
    player.draw_hit_box(window)
    pygame.display.update()

player = Mario(200, 410, 64, 64)
run  = True

while run:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    player.move()
    gameWindow()
pygame.quit()
