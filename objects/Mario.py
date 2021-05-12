import pygame
import os
from pygame.locals import *
pygame.init()

# window = pygame.display.set_mode((500,500))
# pygame.display.set_caption("Mario")

width_screen = 600
height_screen = 224
width = 32
height = 32

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
        #Mario Die
        if self.y + 32 == 448:
            window.blit(deadImage, (self.x, self.y))
            self.y = 480
        
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
            # if self.vel_y == -15:

            if keys[pygame.K_SPACE] == False:
                self.isJump = False

        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
	        self.vel_y = 10

        self.y += self.vel_y
        # if self.y > 448 : 
        #     self.y = 416
        #     self.vel_y = 10
        
        #collision
        hit_box = (abs(bg.bgX) + self.x, self.y, 32, 32)
        hitBox = pygame.Rect(abs(bg.bgX) + self.x, self.y, 32, 32)
        keys = pygame.key.get_pressed()
        hit_block = []
        touch_ground = []

        for i in bg.block:
            i = pygame.Rect(i[0], i[1], i[2], i[3])
            if i.colliderect(hit_box[0], self.y , 32, 32):
                hit_block.append(i)

        for i in bg.ground:
            i = pygame.Rect(i[0], i[1], i[2], i[3])
            if i.colliderect(hit_box[0], self.y , 32, 32):
                touch_ground.append(i)

        for i in touch_ground:
            if i.colliderect(hitBox[0], self.y, 32, 32):
                self.y = i[1] - 32
                self.vel = 0

        for j in hit_block:
            if self.isRight:
                while j.colliderect(hitBox[0], self.y, 32, 32):
                    self.x -= self.vel_x 
                    break
            if self.isLeft:
                while j.colliderect(hitBox[0], self.y, 32, 32):
                    self.x += self.vel_x
                    break
            if self.vel_y > 0:
                while j.colliderect(hitBox[0], self.y, 32, 32):
                    self.y -= 1
                    self.vel = 0
                    
            elif self.vel_y < 0:
                while j.colliderect(hitBox[0], self.y, 32, 32):
                    self.y += 1
                    self.vel = 0
                    
           
            # #x collision
            # #right
            # if i.colliderect(hitBox[0], self.y, 32, 32):
            #     self.vel_x = 0
            #     self.x = hit_box[0] - abs(bg.bgX) - 32
            #     self.y = i[1] + i[3] - 32
            #     print(0)
            # #left
            # if i.colliderect(hitBox[0] - self.vel_x, self.y , 32, 32):    
            #     self.vel_x = 0
            #     self.x = hit_box[0] - abs(bg.bgX) + 5
            #     self.y = i[1] + i[3] - 32
            #     print(1)

            # else:
            #     self.vel_x = 3
            
            #y collision
            
            #     #under
            #     if self.vel_y < 0:
            #         self.y = j[1] + j[3]
            #         self.vel_y = 0
            #     #above
            #     elif self.vel_y >= 0:
            #         self.y = j[1] - 32
            #         self.vel_y = 0
            # else: 
            #     self.vel_x = 3
                
                
            
            


                    


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
        
#     player.move()
#     gameWindow()
# pygame.quit()
