# EndgameChess
# MIT License
# Copyright (c) [2023]
# J. French
# emailjakefrench@googlemail.com

board = [   ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']   ]




import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = HEIGHT = 800
BOARD_SIZE = 8
SQUARE_SIZE = WIDTH // BOARD_SIZE
WHITE = (255, 255, 255)
BLACK = (112, 128, 144)
FONT = pygame.font.Font(None, 36)
cell = ''
allPieces = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', 'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p', 'd']

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endgame Engine")


pieces = { }
for p in allPieces:
    temp = pygame.image.load('pieces/' + p +  '.png')
    temp = pygame.transform.scale(temp, (int(temp.get_size()[0] / int(WIDTH // (WIDTH/5))),
                                              int(temp.get_size()[1] / int(WIDTH // (WIDTH/5)))))
    pieces[p] = temp

def cellToPixels(cell):
    py = -15 + (75*int(cell[1])-1)
    #(-5 + (75 * 4),  * 4)))
    pass
    return 5, py

def rowcolToPosition(p, row, col):
    x, y = (SQUARE_SIZE*col), -(SQUARE_SIZE/15) + (SQUARE_SIZE*row)
    if 'p' in p or 'P' in p:
        y -= 10
    return x, y

# Function to get cell location from mouse click
def get_cell_from_click(x, y):
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    if 0 <= col < BOARD_SIZE and 0 <= row < BOARD_SIZE:
        # Convert col (0-7) to letter (A-H) and row (0-7) to number (1-8)
        col_letter = chr(ord('A') + col)
        row_number = str(8 - row)
        return col_letter + row_number
    else:
        return None


# Main game loop
running = True
while running:
    cell = None
    px, py = None, None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button clicked
                x, y = event.pos
                cell = get_cell_from_click(x, y)
                px, py = cellToPixels(cell)

    # Draw the chess board
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            p = board[row][col]
            if p in allPieces:
                screen.blit(pieces[p],  rowcolToPosition(p, row, col))
    if cell:
        print("Clicked cell:", cell)


    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
