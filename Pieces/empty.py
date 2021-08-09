from Pieces.piece import Piece


class Empty(Piece):
    """No piece"""

    def __init__(self):
        """Initialize empty piece attributes"""
        super().__init__()
        self.display = 'Empty'
        self.set_color(None)

    # def move():