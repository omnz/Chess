from Pieces.piece import Piece


class Bishop(Piece):
    """Bishop piece"""

    def __init__(self):
        """Initialize piece attributes"""
        super().__init__()
        self.display = 'B'
    # def move():