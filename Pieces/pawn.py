from Pieces.piece import Piece


class Pawn(Piece):
    """Pawn piece"""

    def __init__(self):
        """Initialize piece attributes"""
        super().__init__()
        self.display = 'P'
    # def move():

    def check_position(self, board, position):
        row = position[0]
        col = position[1]
        board_pos = board.board[row][col]
        piece = board_pos['piece']['piece']

        print(self.get_position())
        print(piece.get_position())

        if(self.get_color() == 'white'):
            if(self.get_position()[0] < piece.get_position()[0]):
                return 0
        return self