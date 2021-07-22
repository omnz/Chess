from Pieces.piece import Piece


class Rook(Piece):
    """Rook piece"""

    def __init__(self):
        """Initialize piece attributes"""
        super().__init__()
        self.display = 'R'
    # def move():