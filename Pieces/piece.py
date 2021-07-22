class Piece:
    def __init__(self):
        self.can_move = False
    
    def flip_can_move(self):
        """Switch whether the piece can move or not"""
        self.can_move = not self.can_move