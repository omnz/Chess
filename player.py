from Pieces.pawn import Pawn
from Pieces.rook import Rook
from Pieces.bishop import Bishop
from Pieces.king import King
from Pieces.knight import Knight
from Pieces.queen import Queen

class Player:
    def __init__(self, name):
        """Initialize player's attributes and pieces"""
        self.name = name
        self.pieces = []
        self.isTurn = False
        self.piece_color = None
        
        self.build_pieces()
    
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
        """Switch isTurn to True/False"""
        self.isTurn != self.isTurn

    def build_pieces(self):
        """Build list of all pieces"""
        for p in range(0, 8):
            self.pieces.append(Pawn())
        
        otherPieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for p in otherPieces:
            self.pieces.append(p())
        
    # def checkKing():