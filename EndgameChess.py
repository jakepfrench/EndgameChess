# EndgameChess
# MIT License
# Copyright (c) [2023]
# J. French
# emailjakefrench@googlemail.com
import json

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
        pygame.display.set_caption("Endgame Engine [(s) save / (l) load / just play]")


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

    def highlightMove(self, pos):
        if pos is not None:
            r, c = int(pos[1]) - 1, (ord(pos[0]) - ord('a'))
            p = self.board[r][c]
            if p:
                s = pygame.Surface((100, 100))
                s.set_alpha(64)
                s.fill((255, 255, 0))
                self.screen.blit(s, (c * 100, (7 * 100) - (r * 100)))
                return True
        return False

    def clickTocell(self, xy):
        col = int(xy[0] * (self.BOARD_SIZE / self.WIDTH))
        row = int(xy[1] * (self.BOARD_SIZE / self.HEIGHT))
        if 0 <= col < self.BOARD_SIZE and 0 <= row < self.BOARD_SIZE:
            col_letter = chr(ord('a') + col)
            row_number = str(8 - row)
            return col_letter, row_number
        else:
            return None

    def rowcolToPosition(self, p, r, c):
        x, y = (self.SQUARE_SIZE*c), -(self.SQUARE_SIZE/15) + (self.SQUARE_SIZE*r)
        if 'p' in p or 'P' in p:
            y -= 10
        return x, y

    def render(self):
        for r in range(self.BOARD_SIZE):
            for c in range(self.BOARD_SIZE):
                if (r + c) % 2 == 0:
                    color = self.WHITE
                else:
                    color = self.BLACK
                pygame.draw.rect(self.screen, color, (
                c * self.SQUARE_SIZE, r * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))
                p = self.board[r][c]
                if p in self.PIECES:
                    self.screen.blit(self.pieces[p], self.rowcolToPosition(p, r, c))
        pygame.display.flip()

    def event(self):
        # run through all possible eventrs
        for event in pygame.event.get():
            # if quit
            if event.type == pygame.QUIT:
                engine.running = False
            # if load or save
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    with open('EndgameBoard.json', 'w') as json_file:
                        json.dump(self.board, json_file, indent=4)
                elif event.key == pygame.K_l:
                    try:
                        with open("EndgameBoard.json") as json_file:
                            self.board = json.load(json_file)
                    except:
                        print('error')
            # if mouse button is pressed, the game's afoot
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = self.clickTocell(event.pos)
                print(pos)
                self.highlightMove(pos)



engine = EndgameChess(debug = False, screenSize = 800, directory = 'pieces')
while engine.running:
    engine.event()
    engine.render()

pygame.quit()
sys.exit()



