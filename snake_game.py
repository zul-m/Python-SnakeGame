# Set up the game window and initialize Pygame
import pygame
import random
import time

pygame.init()

# Define the window size
window_width = 800
window_height = 600

# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define the Snake class
class Snake:
    def __init__(self):
        self.size = 1
        self.positions = [(window_width // 2, window_height // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (0, 255, 0)  # Green
    
    def get_head_position(self):
        return self.positions[0]
    
    def move(self):
        current_head_position = self.get_head_position()
        x, y = self.direction
        new_head_position = ((current_head_position[0] + (x * GRIDSIZE)) % window_width,
                             (current_head_position[1] + (y * GRIDSIZE)) % window_height)
        if len(self.positions) > 2 and new_head_position in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new_head_position)
            if len(self.positions) > self.size:
                self.positions.pop()
    
    def reset(self):
        self.size = 1
        self.positions = [(window_width // 2, window_height // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
    
    def draw(self):
        for position in self.positions:
            pygame.draw.rect(window, self.color, (position[0], position[1], GRIDSIZE, GRIDSIZE))

# Define the Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (255, 0, 0)  # Red
        self.randomize_position()
    
    def randomize_position(self):
        self.position = (random.randint(0, window_width // GRIDSIZE - 1) * GRIDSIZE,
                         random.randint(0, window_height // GRIDSIZE - 1) * GRIDSIZE)
    
    def draw(self):
        pygame.draw.rect(window, self.color, (self.position[0], self.position[1], GRIDSIZE, GRIDSIZE))

# Define game constants and variables
GRIDSIZE = 20
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

snake = Snake()
food = Food()

score = 0
clock = pygame.time.Clock()

# Set up the game loop
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_UP]:
                snake.direction = UP
