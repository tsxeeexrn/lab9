import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLOCK_SIZE = 20
snake_speed = 10
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def draw_snake(block_size, snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], block_size, block_size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def gameLoop():
    global snake_speed
    game_over = False
    game_close = False
    x = WIDTH / 2
    y = HEIGHT / 2
    x_change = 0
    y_change = 0
    snake_list = []
    snake_length = 1
    foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_weight = random.randint(1, 3)

    food_timer = 5 * clock.get_fps()
    score = 0
    level = 1
    foods_eaten = 0
    while not game_over:
        while game_close:
            screen.fill(BLACK)
            message("Проиграл! Q - выйти, C - заново", RED)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        x += x_change
        y += y_change
        screen.fill(BLACK)
        food_color = [(128, 0, 0), (200, 0, 0), (255, 0, 0)][food_weight - 1]
        pygame.draw.rect(screen, food_color, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True
        draw_snake(BLOCK_SIZE, snake_list)
        score_text = score_font.render("Счет: " + str(score), True, WHITE)
        level_text = score_font.render("Уровень: " + str(level), True, WHITE)
        screen.blit(score_text, [0, 0])
        screen.blit(level_text, [0, 40])
        pygame.display.update()
        if x == foodx and y == foody:
            while True:
                foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
                foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
                food_on_snake = False
                for segment in snake_list:
                    if segment[0] == foodx and segment[1] == foody:
                        food_on_snake = True
                        break
                if not food_on_snake:
                    break

            food_weight = random.randint(1, 3)
            food_timer = 5 * clock.get_fps()

            snake_length += 1
            score += 10 * food_weight
            foods_eaten += 1
            if foods_eaten >= 3:
                level += 1
                foods_eaten = 0
                snake_speed += 2
        food_timer -= 1
        if food_timer <= 0:
            while True:
                foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
                foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
                food_on_snake = False
                for segment in snake_list:
                    if segment[0] == foodx and segment[1] == foody:
                        food_on_snake = True
                        break
                if not food_on_snake:
                    break

            food_weight = random.randint(1, 3)
            food_timer = 5 * clock.get_fps()

        clock.tick(snake_speed)
    pygame.quit()
    sys.exit()

gameLoop()