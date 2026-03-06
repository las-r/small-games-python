import pygame
import random

# lights out
# made by las-r on github

# initialize pygame
pygame.init()

# constants
WIDTH, HEIGHT = 400, 400 # screen size
GRID_SIZE = 4 # grid size
CELL_SIZE = WIDTH // GRID_SIZE # size of each cell

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 100)

# functions
def draw_grid():
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            color = YELLOW if grid[r][c] else BLACK
            pygame.draw.rect(screen, color, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, WHITE, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def toggle_light(row, col):
    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
        grid[row][col] = 1 - grid[row][col]
    
    # toggle adjacent cells
    if row > 0: grid[row - 1][col] = 1 - grid[row - 1][col]
    if row < GRID_SIZE - 1: grid[row + 1][col] = 1 - grid[row + 1][col]
    if col > 0: grid[row][col - 1] = 1 - grid[row][col - 1]
    if col < GRID_SIZE - 1: grid[row][col + 1] = 1 - grid[row][col + 1]

def check_win():
    return all(cell == 0 for row in grid for cell in row)

# grid
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
for _ in range(10):
    row, col = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
    toggle_light(row, col)

# setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lights Out")

# run
running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // CELL_SIZE, x // CELL_SIZE
            toggle_light(row, col)
            if check_win():
                print("You won!")
                running = False

# Quit
pygame.quit()
