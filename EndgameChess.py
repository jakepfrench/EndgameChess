# EndgameChess
# MIT License
# Copyright (c) [2023]
# J. French
# emailjakefrench@googlemail.com

import pygame
import sys

class EndgameChess:
    def __init__(self, debug=False, screenSize=800, directory='pieces'):
        pygame.init()
        # constants
        self.WIDTH = self.HEIGHT = screenSize
        self.BOARD_SIZE = 8
        self.SQUARE_SIZE = self.WIDTH // self.BOARD_SIZE
        self.WHITE = (255, 255, 255)
        self.BLACK = (220, 220, 220)
        self.HIGHLIGHT = (255, 255, 0)
        pygame.font.Font(None, 36)
        self.PIECES = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', 'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p', 'd']

        # variables
        self.running = True
        self.debug = debug
        self.board = self.initialize()
        self.pieces = self.load(directory)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Endgame Engine")

    def initialize(self):
        board = [   ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
                    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']   ]
        return board
    def load(self, directory):
        pieces = { }
        for p in self.PIECES:
            pic = pygame.image.load(directory + '/' + p + '.png')
            pic = pygame.transform.scale(pic, (int(pic.get_size()[0] / int(self.WIDTH // (self.WIDTH/5))),
                                                    int(pic.get_size()[1] / int(self.WIDTH // (self.WIDTH/5)))))
            pieces[p] = pic
        return pieces

    def getClick(self):
        pass


    def clickTocell(self):
        pass

    def rowcolToPosition(self, p, r, c):
        x, y = (self.SQUARE_SIZE*c), -(self.SQUARE_SIZE/15) + (self.SQUARE_SIZE*r)
        if 'p' in p or 'P' in p:
            y -= 10
        return x, y

    def render(self):
        for r in range(self.BOARD_SIZE):
            for c in range(self.BOARD_SIZE):
                color = self.WHITE if (r + c) % 2 == 0 else self.BLACK
                pygame.draw.rect(self.screen, color, (
                c * self.SQUARE_SIZE, r * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))
                p = self.board[r][c]
                if p in self.PIECES:
                    self.screen.blit(self.pieces[p], self.rowcolToPosition(p, r, c))
        pygame.display.flip()



#engine = EndgameChess(debug = False, screenSize = 800, directory = 'pieces')
#while engine.running:
#    engine.render()
#pygame.quit()
#sys.exit()








# Function to get cell location from mouse click
#def get_cell_from_click(x, y):
#    col = x // SQUARE_SIZE
#    row = y // SQUARE_SIZE
#    if 0 <= col < BOARD_SIZE and 0 <= row < BOARD_SIZE:
#        # Convert col (0-7) to letter (A-H) and row (0-7) to number (1-8)
#        col_letter = chr(ord('A') + col)
#        row_number = str(8 - row)
#        return col_letter.lower() + row_number
#    else:
#        return None


pygame.init()
pygame.display.set_mode((100, 100))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
sys.exit()


#        elif event.type == pygame.MOUSEBUTTONDOWN:
#            if event.button == 1:  # Left mouse button clicked
#                x, y = event.pos
#                cell = get_cell_from_click(x, y)
#
#    # Draw the chess board
#    for row in range(BOARD_SIZE):
#        for col in range(BOARD_SIZE):
#            color = WHITE if (row + col) % 2 == 0 else BLACK
#            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
#            p = board[row][col]
#            if p in allPieces:
#                screen.blit(pieces[p],  rowcolToPosition(p, row, col))
#    if cell:
#        r, c = int(cell[1])-1, (ord(cell[0]) - ord('a'))
#        p = board[r][c]
#        if p in allPieces:
#            print("Clicked cell:", p, cell, r, c)
#            s = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))  # the size of your rect
#            s.set_alpha(128)  # alpha level
#            s.fill((255,255,0))  # this fills the entire surface
#            screen.blit(s, (c * SQUARE_SIZE, (7 * SQUARE_SIZE) - (r * SQUARE_SIZE)))  # (0,0) are the top-left coordinates
#
#
#        #pygame.draw.rect(screen, (255,255,204, 255)  , (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
#
#
#    pygame.display.flip()
#
# Quit Pygame
#pygame.quit()
#sys.exit()
