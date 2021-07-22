from Pieces.piece import Piece


class Pawn(Piece):
    """Pawn piece"""

    def __init__(self):
        """Initialize piece attributes"""
        super().__init__()
        self.display = 'P'
    # def move():