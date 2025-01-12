# Importing necessary libraries 
import pygame 
import time 
import random 
# Initialize Pygame 
pygame.init() 
# Screen dimensions and colors 
screen_width, screen_height = 600, 400 
game_display = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption('Snake Game') 
# Colors 
black = (0, 0, 0) 
white = (255, 255, 255) 
red = (213, 50, 80) 
green = (0, 255, 0) 
blue = (50, 153, 213) 
 
# Snake properties 
snake_block = 10 
snake_speed = 15 
 
# Fonts 
font_style = pygame.font.SysFont("bahnschrift", 25) 
score_font = pygame.font.SysFont("comicsansms", 35) 
 
# Score function 
def display_score(score): 
    value = score_font.render(f"Score: {score}", True, blue) 
    game_display.blit(value, [0, 0]) 
 
# Snake function 
def draw_snake(snake_block, snake_list): 
    for x in snake_list: 
        pygame.draw.rect(game_display, black, [x[0], x[1], 
snake_block, snake_block]) 
 
# Message function 
def message(msg, color): 
    mesg = font_style.render(msg, True, color) 
    game_display.blit(mesg, [screen_width / 6, screen_height / 3]) 
 
# Game loop 
def game_loop(): 
    game_over = False 
    game_close = False 
 
    x1, y1 = screen_width / 2, screen_height / 2 
    x1_change, y1_change = 0, 0 
 
    snake_list = [] 
    snake_length = 1 
 
    food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0 
    food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0 
 
    clock = pygame.time.Clock() 
    score = 0 
 
    while not game_over: 
 
        while game_close: 
            game_display.fill(white) 
            message("You Lost! Press Q-Quit or C-Play Again", red) 
            display_score(snake_length - 1) 
            pygame.display.update() 
 
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_q: 
                        game_over = True 
                        game_close = False 
                    elif event.key == pygame.K_c: 
                        game_loop() 
 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                game_over = True 
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT: 
                    x1_change = -snake_block 
                    y1_change = 0 
                elif event.key == pygame.K_RIGHT: 
                    x1_change = snake_block 
                    y1_change = 0 
                elif event.key == pygame.K_UP: 
                    y1_change = -snake_block 
                    x1_change = 0 
                elif event.key == pygame.K_DOWN: 
                    y1_change = snake_block 
                    x1_change = 0 
 
        # Snake movement boundaries 
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0: 
            game_close = True 
 
        x1 += x1_change 
        y1 += y1_change 
        game_display.fill(white) 
 
        pygame.draw.rect(game_display, green, [food_x, food_y, snake_block, snake_block]) 
 
        snake_head = [x1, y1] 
        snake_list.append(snake_head) 
        if len(snake_list) > snake_length: 
            del snake_list[0] 
 
        for x in snake_list[:-1]: 
            if x == snake_head: 
                game_close = True 
 
        draw_snake(snake_block, snake_list) 
        display_score(snake_length - 1) 
 
        pygame.display.update() 
 
        # Snake eats food 
        if x1 == food_x and y1 == food_y: 
            food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0 
            food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0 
            snake_length += 1 
            score += 10 
 
        clock.tick(snake_speed) 
 
    pygame.quit() 
    quit() 
 
# Start the game 
game_loop()