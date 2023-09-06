import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
GAME_WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game: Silicon Workshop Python course")

# Set up the game clock
GAME_CLOCK = pygame.time.Clock()

# Set up the game variables
SNAKE_BLOCK_SIZE = 24
SNAKE_SPEED = 10

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define the Snake class
class Snake:
    def __init__(self):
        self.head_x = WINDOW_WIDTH / 2
        self.head_y = WINDOW_HEIGHT / 2
        self.body = [(self.head_x, self.head_y)]
        self.direction = "right"
    
    def move(self):
        if self.direction == "right":
            self.head_x += SNAKE_BLOCK_SIZE
        elif self.direction == "left":
            self.head_x -= SNAKE_BLOCK_SIZE
        elif self.direction == "up":
            self.head_y -= SNAKE_BLOCK_SIZE
        elif self.direction == "down":
            self.head_y += SNAKE_BLOCK_SIZE
        
        self.body.insert(0, (self.head_x, self.head_y))
        self.body.pop()
    
    def grow(self):
        self.body.append(self.body[-1])
    
    def draw(self):
        for block in self.body:
            pygame.draw.rect(GAME_WINDOW, GREEN, (block[0], block[1], SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE))

# Define the Food class
class Food:
    def __init__(self):
        self.x = random.randrange(0, WINDOW_WIDTH - SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE)
        self.y = random.randrange(0, WINDOW_HEIGHT - SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE)
    
    def draw(self):
        pygame.draw.rect(GAME_WINDOW, RED, (self.x, self.y, SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE))

# Set up the game objects
snake = Snake()
food = Food()

# Set up the game loop
game_running = True
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.direction != "left":
                snake.direction = "right"
            elif event.key == pygame.K_LEFT and snake.direction != "right":
                snake.direction = "left"
            elif event.key == pygame.K_UP and snake.direction != "down":
                snake.direction = "up"
            elif event.key == pygame.K_DOWN and snake.direction != "up":
                snake.direction = "down"
    
    # Move the snake
    snake.move()
    
    # Check for collisions
    if snake.body[0][0] < 0 or snake.body[0][0] >= WINDOW_WIDTH or snake.body[0][1] < 0 or snake.body[0][1] >= WINDOW_HEIGHT:
        game_running = False
    elif snake.body[0] in snake.body[1:]:
        game_running = False
    elif snake.body[0][0] == food.x and snake.body[0][1] == food.y:
        snake.grow()
        food = Food()
    
    # Draw the game objects
    GAME_WINDOW.fill(BLACK)
    snake.draw()
    food.draw()
    pygame.display.update()
    
    # Set the game clock tick rate
    GAME_CLOCK.tick(SNAKE_SPEED)

# Quit pygame
pygame.quit()