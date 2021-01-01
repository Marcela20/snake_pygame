import pygame
import sys
from pygame.locals import *
import random

pygame.init()


def message(msg, color):
    mesg = font.render(msg, True, color)
    window.blit(mesg, [(dis_width / 2) - 100, (dis_height / 2) - 30])


def draw_snake():
    for element in whole_snake:
        pygame.draw.rect(window, (0, 255, 0), element)
    pygame.display.update()


def snake_elongation():
    x = whole_snake[-1].x
    y = whole_snake[-1].y
    whole_snake.append(pygame.Rect(x, y, 20, 20))


def move_snake(dir):
    step = 20
    list_of_old = []
    for elem in range(1, len(whole_snake)):
        list_of_old.append([whole_snake[elem].x, whole_snake[elem].y])
        if elem < 2:
            whole_snake[elem].x = whole_snake[elem - 1].x
            whole_snake[elem].y = whole_snake[elem - 1].y
        else:
            whole_snake[elem].x = list_of_old[-2][0]
            whole_snake[elem].y = list_of_old[-2][1]

    if dir == "RIGHT":
        snake_head.x += step
    elif dir == "LEFT":
        snake_head.x -= step
    elif dir == "UP":
        snake_head.y -= step
    elif dir == "DOWN":
        snake_head.y += step


# window
dis_width = 1000
dis_height = 500
window_size = (dis_width, dis_height)
window = pygame.display.set_mode(window_size, 0, 32)
pygame.display.set_caption("snake")
# snake, font, FPS
snake_lenght = 500
snake_width = 260
FPS = 20
fpsClock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 80)
direction = ''
# colors
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

while True:
    whole_snake = [pygame.Rect(snake_lenght, snake_width, 20, 20)]
    snake_head = whole_snake[0]
    food_for_snake = pygame.Rect(random.randrange(0, 980, 20), random.randrange(0, 480, 20), 20, 20)

    while True:
        window.fill((0, 0, 0))
        fpsClock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        direction = 'LEFT'
        if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 'RIGHT'

            if event.key == pygame.K_LEFT:
                direction = 'LEFT'

            if event.key == pygame.K_UP:
                direction = 'UP'

            if event.key == pygame.K_DOWN:
                direction = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        # touching screen border
        if snake_head.x > 980 or snake_head.x < 0 or snake_head.y > 480 or snake_head.y < 0:
            message("loser", red)
            step = 0
            # add_button()

            font_obj = pygame.font.Font('freesansbold.ttf', 32)
            text_surface_obj = font_obj.render('play again!', True, white, blue)
            text_rect_obj = text_surface_obj.get_rect()
            button = window.blit(text_surface_obj, text_rect_obj)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                    break
            pygame.display.update()
        # eating
        if snake_head.x == food_for_snake.x and snake_head.y == food_for_snake.y:
            food_for_snake = pygame.Rect(random.randrange(0, 980, 20), random.randrange(0, 480, 20), 20, 20)
            snake_elongation()

        move_snake(direction)

        # drawing
        food = pygame.draw.rect(window, (100, 100, 100), food_for_snake)
        draw_snake()
