import pygame
import os

pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Mario")

# run1 = pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run1.png")), (48,48))
# run2 = pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run2.png")), (48,48))
# run3 = pygame.transform.scale(pygame.image.load(os.path.join("img", "mario_run2.png")), (48,48))
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
        player.horizonFacing = 'left'
        player.isRight = False
    elif keys[pygame.K_RIGHT] and player.x < 500 - player.width - player.vel:
        player.x += player.vel
        player.isRight = True
        player.horizonFacing = 'right'
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