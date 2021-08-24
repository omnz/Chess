from Pieces.piece import Piece


class Empty(Piece):
    """No piece"""

    def __init__(self):
        """Initialize empty piece attributes"""
        super().__init__()
        self.display = 'Empty'
        self.set_color(None)

    def check_position(self, board, player, p1):
        """Returns '1' if position is valid."""
        
        possible_positions = []
        
        return possible_positions