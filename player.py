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
        
        # self.build_pieces()
    
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
        
        # Switch pieces to be able to move/not move
        for piece in self.pieces:
            piece['piece'].flip_can_move()

    def build_pieces(self, color):
        """Build list of all pieces"""
        for p in range(0, 8):
            self.pieces.append({'piece': Pawn(), 'img': pygame.image.load(f'Sprites/pawn_{color}.png')})
        
        otherPieces = [
            {'piece': Rook(), 'img': pygame.image.load(f'Sprites/rook_{color}.png')},
            {'piece': Knight(), 'img': pygame.image.load(f'Sprites/knight_{color}.png')},
            {'piece': Bishop(), 'img': pygame.image.load(f'Sprites/bishop_{color}.png')},
            {'piece': Queen(), 'img': pygame.image.load(f'Sprites/queen_{color}.png')}, 
            {'piece': King(), 'img': pygame.image.load(f'Sprites/king_{color}.png')},
            {'piece': Bishop(), 'img': pygame.image.load(f'Sprites/bishop_{color}.png')},
            {'piece': Knight(), 'img': pygame.image.load(f'Sprites/knight_{color}.png')},
            {'piece': Rook(), 'img': pygame.image.load(f'Sprites/rook_{color}.png')}]

        for p in otherPieces:
            self.pieces.append(p)
        
    # def checkKing():
        # if king is in danger
        # if king is no longer in play then game over