class Piece:
    def __init__(self):
        self.can_move = False
        self.position = None
        self.color = None
    
    def flip_can_move(self):
        """Switch whether the piece can move or not"""
        self.can_move = not self.can_move

    def get_position(self):
        return self.position
    
    def set_position(self, row, col):
        self.position = (row, col)

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color