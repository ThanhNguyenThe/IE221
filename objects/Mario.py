import pygame
import os

pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Mario")
walkRight = [pygame.image.load(os.path.join("img", "mario_run1.png")),
            pygame.image.load(os.path.join("img", "mario_run2.png")),
            pygame.image.load(os.path.join("img", "mario_run3.png"))]

walkLeft = [pygame.transform.flip(pygame.image.load(os.path.join("img", "mario_run1.png")), True, False),
            pygame.transform.flip(pygame.image.load(os.path.join("img", "mario_run2.png")), True, False),
            pygame.transform.flip(pygame.image.load(os.path.join("img", "mario_run3.png")), True, False)]

deadImage = pygame.image.load(os.path.join("img", "mario_die.png"))
jumpImage = pygame.image.load(os.path.join("img", "mario_jump.png"))
char = pygame.image.load(os.path.join("img", "mario_stand.png"))

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
        self.walkCount = 0 
        self.jumpCount = 10
        
    def draw(self, window):
        if self.walkCount + 1 >= 9:
            self.walkCount =  0
        if self.isLeft:
            window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.isRight:
            window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            window.blit(char, (self.x, self.y))

def gameWindow():
    window.fill([255,255,255])
    player.draw(window)

    pygame.display.update()

player = Mario(200, 410, 64, 64)
run  = True

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel
        player.isLeft = True
        player.isRight = False
    elif keys[pygame.K_RIGHT] and player.x < 500 - player.width - player.vel:
        player.x += player.vel
        player.isRight = True
        player.isLeft = False
    else:
        player.isRight = False
        player.isLeft = False
        player.walkCount = 0

    if not(player.isJump):
        if keys[pygame.K_SPACE]:
            player.isJump = True
            player.isRight = False
            player.isLeft = False
            player.walkCount = 0
    else:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10

    gameWindow()
pygame.quit()