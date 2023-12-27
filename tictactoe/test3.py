import pygame
import numpy as np

# Define the board as a 3x3 NumPy array
def create_board():
    board = np.zeros((3, 3))
    return board

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 600, 600

# Create the window
screen = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption('Tic-Tac-Toe')

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Draw the empty tic-tac-toe board
screen.fill(white)
line_width = 10
# Vertical lines
pygame.draw.line(screen, black, (width // 3, 0), (width // 3, height), line_width)
pygame.draw.line(screen, black, (2 * width // 3, 0), (2 * width // 3, height), line_width)
# Horizontal lines
pygame.draw.line(screen, black, (0, height // 3), (width, height // 3), line_width)
pygame.draw.line(screen, black, (0, 2 * height // 3), (width, 2 * height // 3), line_width)

# Update the display
pygame.display.flip()

# Game loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()