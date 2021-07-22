from Pieces.piece import Piece


class Queen(Piece):
    """Queen piece"""

    def __init__(self):
        """Initialize piece attributes"""
        super().__init__()
        self.display = 'Q'
    # def move():