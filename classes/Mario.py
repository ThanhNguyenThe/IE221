import pygame
import os
from pygame.locals import *
pygame.init()

# window = pygame.display.set_mode((500,500))
# pygame.display.set_caption("Mario")

mario_width_pos = 800
height_screen = 448
width = 32
height = 32

#load các sprite đi qua phải
walkRight = [pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run1.png")), (width, height)),
            pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run2.png")), (width, height)),
            pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run3.png")), (width, height))]

#load các sprite đi qua trái
walkLeft = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run1.png")), (width, height)), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run2.png")), (width, height)), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run3.png")), (width, height)), True, False)]

#sprite nhảy, chết
deadImage = pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_die.png")), (width, height))
jumpImage = pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_jump.png")), (width, height))
char = pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_stand.png")), (width, height))
clock = pygame.time.Clock()

class Mario(pygame.sprite.Sprite):
    """
    Nhân vật Mario
        Attributes:
            x: int, tọa độ x
            y: int, tọa độ y
            width: int, độ rộng
            height: int, độ dài
            rect: pygame.Rect, hcn của tọa độ
            vel_x: int, vận tốc chiều ngang
            vel_y: int, vận tốc chiều dọc
            isJump: bool, cờ kiểm tra nhảy
            isLeft: bool, cờ kiểm tra xoay mặt trái
            isRight: bool, cờ kiểm tra xoay mặt phải
            isDie: bool, cờ kiểm tra chết
            horizonFacing: str, cờ kiểm tra xoay mặt phải hay trái khi nhảy
            walkCount: int, thay đổi sprite
            jumpCount: int, giới hạn độ cao khi nhảy (đã xóa chức năng này)

        Methods:
            draw(window): Thay đổi sprite liên tục khi di chuyển.
            draw_hit_box(window): Vẽ hitbox.
            move(bg):   Kích hoạt cờ để thay đổi sprite khi di chuyển và di chuyển.
                    Xử lý va chạm và thêm trọng lực.
            dead(enemy, window, bg): Kiểm tra khi nào mario chết.
    """
    def __init__(self, x, y, width, height):
        """Khởi tạo."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.vel_x = 3 #vận tốc x
        self.vel_y = 3 #vận tốc y
        self.isJump = False   #các cờ check thay đổi sprite
        self.isLeft = False
        self.isRight = False
        self.isDie = False
        self.horizonFacing = 'right'
        self.walkCount = 0 
        self.jumpCount = 10 #Nếu cần giới hạn độ cao khi nhảy thì dùng

        
    def draw(self, window): 
        """Thay đổi sprite liên tục khi di chuyển."""
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
        # if self.isDie:
        #     self.y = 500
        #     window.blit(deadImage, (self.x, self.y))

        
    def draw_hit_box(self, window):
        """Vẽ hitbox."""
        hitBox = (self.x, self.y, 32, 32)
        pygame.draw.rect(window, [0, 255, 0], hitBox, 2)     


    def move(self, bg):
        """
        Kích hoạt cờ để thay đổi sprite khi di chuyển và di chuyển.
        Xử lý va chạm và thêm trọng lực.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > self.vel_x:
            self.x -= self.vel_x
            self.isLeft = True
            self.horizonFacing = 'left'
            self.isRight = False
        elif keys[pygame.K_RIGHT] and self.x < mario_width_pos - self.width - self.vel_x:
            self.x += self.vel_x
            self.isRight = True
            self.horizonFacing = 'right'
            self.isLeft = False
        else:
            self.isRight = False
            self.isLeft = False
            self.walkCount = 0

        if not(self.isJump): #nhảy
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
        if self.y > 448 : 
            self.y = 416
            self.vel_y = 10
        # y collision
        hitBox = (abs(bg.bgX) + self.x, self.y, 32, 32)
        for i in bg.block:
            i = pygame.Rect(i)
            if i.colliderect(hitBox[0], self.y + self.vel_y, 32, 32):
                if self.vel_y < 0:
                    self.y = i[1] + i[3]
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    self.y = i[1] - 32
                    self.vel_y = 0
           #     return False

    def dead(self, enemy, window, bg):
        """Kiểm tra khi nào mario chết."""
        if self.y >= 416: #rớt vực
            window.blit(deadImage, (self.x, self.y))
            return True
        hit_box = pygame.Rect(self.x - bg.bgX, self.y, 32, 32)
        enemy_hitBox = pygame.Rect(enemy.x, enemy.y, 32, 32)
        if hit_box.colliderect(enemy_hitBox) == True:
            # Check neu diem trai cua mario cham enemy nhung diem phai thi ko 
            # Check phai enemy collide voi mario
            if enemy_hitBox.collidepoint(hit_box.midleft) == True and (\
                enemy_hitBox.collidepoint(hit_box.topleft) == True or \
                enemy_hitBox.collidepoint(hit_box.bottomleft) == True) and \
                enemy_hitBox.collidepoint(hit_box.midright) == False and (\
                enemy_hitBox.collidepoint(hit_box.topright) == False or \
                enemy_hitBox.collidepoint(hit_box.bottomright) == False):
                    window.blit(deadImage, (self.x, self.y))
                    return True
            # Check neu diem phai cua mario cham enemy nhung diem trai thi ko 
            # Check trai enemy collide voi mario
            if enemy_hitBox.collidepoint(hit_box.midright) == True and (\
                enemy_hitBox.collidepoint(hit_box.topright) == True or \
                enemy_hitBox.collidepoint(hit_box.bottomright) == True) and \
                enemy_hitBox.collidepoint(hit_box.midleft) == False and (\
                enemy_hitBox.collidepoint(hit_box.topleft) == False or \
                enemy_hitBox.collidepoint(hit_box.bottomleft) == False):
                    window.blit(deadImage, (self.x, self.y))
                    return True
            pass
        else:
            return False

    # def kill(self, enemy, window, bg):
    #     hit_box = pygame.Rect(abs(bg.bgX) + self.x, self.y, 32, 32)
    #     enemy_hitBox = pygame.Rect(abs(bg.bgX) + enemy.x, enemy.y - 4, 32, 34)
    #     if hit_box.colliderect(enemy_hitBox) == True:
    #         #check neu mario collide voi top side enemy 
    #         if enemy_hitBox.collidepoint(hit_box.midbottom) == True and (\
    #             enemy_hitBox.collidepoint(hit_box.bottomleft) == True or \
    #             enemy_hitBox.collidepoint(hit_box.bottomright) == True) and \
    #             enemy_hitBox.collidepoint(hit_box.midtop) == True and (\
    #             enemy_hitBox.collidepoint(hit_box.topleft) == True or \
    #             enemy_hitBox.collidepoint(hit_box.topright) == True):
    #                 enemy.die()

