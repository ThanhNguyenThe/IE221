import pygame
from game.game import *
from data.top3 import *

pygame.init()
pygame.display.set_caption('Mario 1.0')
screen = pygame.display.set_mode((800,484))

click = False

def main_menu():
    while True:

        screen.fill((0, 0, 0))
        message_to_screen('Main menu', white, screen, (325, 20))
        
        mx, my = pygame.mouse.get_pos()

        btn1 = pygame.Rect(300, 150, 200, 30)
        btn2 = pygame.Rect(300, 250, 200, 30)
        btn3 = pygame.Rect(300, 350, 200, 30)
       

        if btn1.collidepoint(mx,my):
            if click:
                start_game(screen)
        if btn2.collidepoint(mx, my):
            if click:
                hall_of_fame()
        if btn3.collidepoint(mx, my):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, (255, 0, 0), btn1)
        pygame.draw.rect(screen, (255, 0, 0), btn2)
        pygame.draw.rect(screen, (255, 0, 0), btn3)
        message_to_screen('Play', white, screen, (370, 150))
        message_to_screen('Ranked', white, screen, (350, 250))
        message_to_screen('Quit', white, screen, (370, 350))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()

def hall_of_fame():
    running = True
    while running:
        screen.fill((0, 0, 0))
        message_to_screen('Ranked', white, screen, (350, 20))
        top_player = top3()
        if (len(top_player) == 0):
            message_to_screen('Nobody has been here!', white, screen, (260, 150))
        else:
            message_to_screen('Name: ' + top_player[0][0] + '   ' + 'Time: ' + str(top_player[0][1]) + 's', white, screen, (280, 150))
            message_to_screen('Name: ' + top_player[1][0] + '   ' + 'Time: ' + str(top_player[1][1]) + 's', white, screen, (280, 250))
            message_to_screen('Name: ' + top_player[2][0] + '   ' + 'Time: ' + str(top_player[2][1]) + 's', white, screen, (280, 350))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()

main_menu()