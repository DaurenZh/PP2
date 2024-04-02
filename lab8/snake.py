import pygame
import random

# Initialize pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of each grid block
BLOCK_SIZE = 20

# Set the speed of the snake
INITIAL_SPEED = 10

# Set the display size
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# Set the font and size
FONT_STYLE = 'freesansbold.ttf'
FONT_SIZE = 30

# Define the game clock
clock = pygame.time.Clock()

# Define the font
font = pygame.font.Font(FONT_STYLE, FONT_SIZE)

# Function to display text on the screen
def display_text(text, color, x, y):
    rendered_text = font.render(text, True, color)
    gameDisplay.blit(rendered_text, (x, y))

# Function to draw the snake
def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(gameDisplay, GREEN, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

# Function to generate random food position
def generate_food():
    food_x = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    return food_x, food_y

# Function to display the score and level
def display_stats(score, level):
    display_text(f"Score: {score}", (255, 255, 255), 10, 10)
    display_text(f"Level: {level}", (255, 255, 255), 10, 40)

# Function to display the game over message
def game_over():
    gameDisplay.fill(RED)
    display_text("Game Over!", BLACK, DISPLAY_WIDTH // 2 - 100, DISPLAY_HEIGHT // 2 - 50)
    display_text("Press Q to Quit or C to Play Again", BLACK, DISPLAY_WIDTH // 2 - 200, DISPLAY_HEIGHT // 2 + 20)
    pygame.display.update()
    # Wait for user to press Q or C
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    game_loop()

# Function to check for border collision
def check_border_collision(x, y):
    if x >= DISPLAY_WIDTH or x < 0 or y >= DISPLAY_HEIGHT or y < 0:
        return True
    return False

# Function to check if the snake hits itself
def check_self_collision(new_head, snake_list):
    for segment in snake_list[:-1]:
        if new_head == segment:
            return True
    return False

# Function to manage the game loop
def game_loop():
    # Initialize variables
    game_over_flag = False
    game_exit = False
    score = 0
    level = 1
    speed = INITIAL_SPEED

    # Initialize snake
    snake_list = []
    snake_length = 1
    snake_x = DISPLAY_WIDTH / 2
    snake_y = DISPLAY_HEIGHT / 2
    snake_x_change = 0
    snake_y_change = 0

    # Initialize food
    food_x, food_y = generate_food()

    while not game_exit:
        while game_over_flag:
            game_over()
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -BLOCK_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = BLOCK_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -BLOCK_SIZE
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = BLOCK_SIZE
                    snake_x_change = 0

        # Update snake position
        snake_x += snake_x_change
        snake_y += snake_y_change

        # Check for border collision or self-collision
        if check_border_collision(snake_x, snake_y) or check_self_collision([snake_x, snake_y], snake_list):
            game_over_flag = True

        # If snake eats food
        if snake_x == food_x and snake_y == food_y:
            score += 1
            snake_length += 1
            food_x, food_y = generate_food()
            if score % 3 == 0:  # Increase level after every 3 foods eaten
                level += 1
                speed += 2  # Increase speed with each level

        # Update snake list
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Refresh the display
        gameDisplay.fill(BLACK)
        pygame.draw.rect(gameDisplay, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        draw_snake(snake_list)
        display_stats(score, level)
        pygame.display.update()

        # Set game speed
        clock.tick(speed)

    pygame.quit()
    quit()

# Set the display size and caption
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Snake Game')

# Start the game loop
game_loop()
