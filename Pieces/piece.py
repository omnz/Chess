class Piece:
    def __init__(self):
        # self.can_move = False
        self.position = None
        self.color = None
        self.index = None
    
    # def flip_can_move(self):
    #     """Switch whether the piece can move or not"""
    #     self.can_move != self.can_move

    def get_position(self):
        return self.position
    
    def set_position(self, row, col):
        self.position = (row, col)

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_index(self, number):
        self.index = number

    def get_index(self):
        return self.index