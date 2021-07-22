from Pieces.piece import Piece


class King(Piece):
    """King piece"""

    def __init__(self):
        """Initialize piece attributes"""
        super().__init__()
        self.display = 'K'
    # def move():