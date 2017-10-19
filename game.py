import pygame
import time, os
import random

pygame.init()

white = (255, 255, 255)
salmon = (250, 128, 114)
red = (255, 0, 0)
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Well Just a Try")

font = pygame.font.SysFont('Comic Sans MS', 20)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, (1200/2, 800/2))

def gameLoop():

    Move_x = 600
    Move_y = 580
    Move_continue_x = 0
    Move_continue_y = 0
    flag_1 = 1
    flag = 1
    flag_2 = 1
    flag_3 = 0

    gameExit = False
    gameOver = False

    randobstacleX = random.randrange(600, 1200)

    lists1 = []
    lists2 = []
    lists3 = []

    pygame.display.update()

    while not gameExit:


        while gameOver == True:
            gameDisplay.fill(salmon)
            message_to_screen("Game Over press C to continue and Q to quit", white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                gameOver = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and Move_y == 580:
                    Move_continue_y = 20
                    flag_3 = 0

            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT:
            #         Move_continue_x = 0
            #     if event.key == pygame.K_RIGHT:
            #         Move_continue_x = 0
            #     if event.key == pygame.K_UP:
            #         Move_continue_y = 0
            #     if event.key == pygame.K_DOWN:
            #         Move_continue_y = 0

        if (Move_y < 620 and Move_y > 540) and (randobstacleX - 50 <= 150+40 and randobstacleX + 40 >= 150-40):
            gameOver = True
            print("True")

        if flag_3 == 0:
            if Move_y <= 580 and Move_y >= 460:
                Move_y -= Move_continue_y
            if Move_y == 460:
                flag_3 = 1

        elif flag_3 == 1:
            if Move_y < 580:
                Move_y += Move_continue_y
            if Move_y == 580:
                flag_3 = 3

        gameDisplay.fill(white)

        if(flag > 5):
            flag = 1
        if(flag_2 > 22):
            flag_2 = 1
        if(flag_1 > 2):
            flag_1 = 1


        lists1 = pygame.image.load(os.path.join('images2', 'image'+str(flag)+'.png'))
        lists2 = pygame.image.load(os.path.join('images31', 'img'+str(flag_2)+'.png'))
        lists3 = pygame.image.load(os.path.join('zombie', 'zombie_walk'+str(flag_1)+'.png'))

        if(randobstacleX <= 0):
            randobstacleX = random.randrange(1200, 1300)
        else:
            randobstacleX -= 20

        print (Move_y)

        gameDisplay.blit(lists2 , (0, 0))
        gameDisplay.blit(pygame.transform.scale(lists1, (120, 90)) , (600/4, Move_y))
        gameDisplay.blit(pygame.transform.scale(lists3, (80, 90)), (randobstacleX, 580))

        clock.tick(12)
        pygame.display.update()
        flag += 1
        flag_2 += 1
        flag_1 += 1


    pygame.quit()
    quit()

gameLoop()
