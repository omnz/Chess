import pygame
from player import Player

class Board:
    """Chess board model"""
    
    def __init__(self):
        """Initialize board attributes"""
        self.rows = 8
        self.cols = 8
        self.board = [[0]*self.cols for _ in range(0, self.rows)]
        self.board_colors = [[0]*self.cols for _ in range(0, self.rows)]
    
    def setup(self, white, black):
        """Setup the initial board state"""
        # Board colors
        alternate = False
        for x in range(0, self.rows):
            for y in range(0, self.cols):
                if alternate == True:
                    self.board[x][y] = {'color': pygame.image.load('Sprites/white.png'), 'piece': 0}
                    alternate = not alternate
                else:
                    self.board[x][y] = {'color': pygame.image.load('Sprites/black.png'), 'piece': 0}
                    alternate = not alternate
            alternate = not alternate
        
        # Board pieces
        for x in range(0, self.rows):
            # Black pieces - Back row
            if x == 0:
                middle_piece = (int)(len(black.pieces)/2)

                for y in range(0, self.cols):
                    self.board[x][y]['piece'] = black.pieces[middle_piece]
                    middle_piece += 1
            
            # Black pieces - Front row
            if x == 1:
                for y in range(0, self.cols):
                    self.board[x][y]['piece'] = black.pieces[y]
            
            # White pieces - Front row
            if x == 6:
                for y in range(0, self.cols):
                    self.board[x][y]['piece'] = white.pieces[y]

            # White pieces - Back row
            if x == 7:
                middle_piece = (int)(len(white.pieces)/2)

                for y in range(0, self.cols):
                    self.board[x][y]['piece'] = white.pieces[middle_piece]
                    middle_piece += 1


    def display(self):
        """Print out the current state of the board"""
        counter = self.cols
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        for row in self.board:
            print(f"{counter} | ", end='')
            counter -= 1

            for piece in row:
                if piece == 0:
                    print(f" {piece} ", end='')
                else:
                    print(f" {piece.display} ", end='')
            print()
        
        # Print line of hyphens
        print("  ", end='')
        for x in range(0, len(letters) * 4 - 6):
            print("-", end='')
        print()
        print("    ", end='')

        # Print list of letters
        for letter in letters:
            print(f" {letter} ", end='')
        print()