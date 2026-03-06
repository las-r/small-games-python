import pygame

# connect four
# made by las-r on github

# initialize pygame
pygame.init()

# constants
WIDTH, HEIGHT = 700, 600 # screen size
ROWS, COLS = 6, 7 # board size
SLOT_RAD = 45 # slot radius in px
FONT = pygame.font.Font(None, 74) # font

# colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# turn
turn = 1
winner = None

# board
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")

def draw_board():
    screen.fill(BLUE)
    for row in range(ROWS):
        for col in range(COLS):
            x = (col + 0.5) * (WIDTH // COLS)
            y = (row + 0.5) * (HEIGHT // ROWS)
            color = BLACK
            if board[row][col] == 1:
                color = RED
            elif board[row][col] == 2:
                color = YELLOW
            pygame.draw.circle(screen, color, (int(x), int(y)), SLOT_RAD)
    if winner:
        text = FONT.render(f"{winner} Wins!", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

def drop_token(col, player):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = player
            return True
    return False

def check_win():
    global winner
    
    # check horizontal, vertical, and diagonal wins
    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] and all(board[row][col + i] == board[row][col] for i in range(4)):
                winner = "Red" if board[row][col] == 1 else "Yellow"
                return
    for row in range(ROWS - 3):
        for col in range(COLS):
            if board[row][col] and all(board[row + i][col] == board[row][col] for i in range(4)):
                winner = "Red" if board[row][col] == 1 else "Yellow"
                return
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] and all(board[row + i][col + i] == board[row][col] for i in range(4)):
                winner = "Red" if board[row][col] == 1 else "Yellow"
                return
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] and all(board[row - i][col + i] == board[row][col] for i in range(4)):
                winner = "Red" if board[row][col] == 1 else "Yellow"
                return

# run
running = True
while running:
    draw_board()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not winner:
            x, y = event.pos
            col = x // (WIDTH // COLS)
            if drop_token(col, turn):
                check_win()
                turn = 3 - turn

# quit
pygame.quit()
