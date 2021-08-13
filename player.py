from Pieces.pawn import Pawn
from Pieces.rook import Rook
from Pieces.bishop import Bishop
from Pieces.king import King
from Pieces.knight import Knight
from Pieces.queen import Queen
import pygame

class Player:
    def __init__(self, name):
        """Initialize player's attributes and pieces"""
        self.name = name
        self.pieces = []
        self.is_turn = False
        self.piece_color = None
    
    def set_name(self, name):
        """Set the player's name"""
        self.name = name
    
    def get_name(self):
        """Return the player's name"""
        return self.name

    def set_piece_color(self, color):
        """Set the player's name"""
        self.piece_color = color
    
    def get_piece_color(self):
        """Return the player's piece color"""
        return self.piece_color

    def turn(self):
        """Switch is_turn and player's pieces' can_move to True/False"""
        self.is_turn = not self.is_turn
        
        # # Switch pieces to be able to move/not move
        # for piece in self.pieces:
        #     piece['piece'].flip_can_move()

    def build_pieces(self, color):
        """Build list of all pieces"""
        for n in range(0, 8):
            self.pieces.append({'piece': Pawn(), 'img': pygame.image.load(f'Sprites/pawn_{color}.png')})

        otherPieces = [
            {'piece': Rook(), 'img': pygame.image.load(f'Sprites/rook_{color}.png'),},
            {'piece': Knight(), 'img': pygame.image.load(f'Sprites/knight_{color}.png')},
            {'piece': Bishop(), 'img': pygame.image.load(f'Sprites/bishop_{color}.png')},
            {'piece': Queen(), 'img': pygame.image.load(f'Sprites/queen_{color}.png')}, 
            {'piece': King(), 'img': pygame.image.load(f'Sprites/king_{color}.png')},
            {'piece': Bishop(), 'img': pygame.image.load(f'Sprites/bishop_{color}.png')},
            {'piece': Knight(), 'img': pygame.image.load(f'Sprites/knight_{color}.png')},
            {'piece': Rook(), 'img': pygame.image.load(f'Sprites/rook_{color}.png')}]

        for p in otherPieces:
            self.pieces.append(p)

        self.set_indexes()

    def set_indexes(self):
        """Set indexes for place in 'pieces' list"""
        count = 0
        for piece in self.pieces:
            piece['piece'].set_index(count)
            count += 1

    def print_pieces(self):
        """Print all of the player's pieces"""
        for piece in self.pieces:
            print(piece)
    
    def promote_piece(self, board, piece, row, col):
        """Promote piece to Queen"""
        index = piece['piece']['piece'].get_index()
        self.pieces[index]['piece'] = Queen()
        self.pieces[index]['piece'].set_color(self.get_piece_color())
        self.pieces[index]['piece'].set_position(row, col)
        self.pieces[index]['piece'].set_index(index)
        self.pieces[index]['piece'].can_move = True
        board.board[row][col]['piece']['img'] = pygame.image.load(f'Sprites/queen_{self.get_piece_color()}.png')
        
    def print_piece_index(self):
        """Print all of a players pieces with their corresponding index"""
        for p in self.pieces:
            print(f"{p['piece']}, {p['piece'].get_index()}")
        print()
