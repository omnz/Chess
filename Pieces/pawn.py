from Pieces.piece import Piece
from Pieces.empty import Empty


class Pawn(Piece):
    """Pawn piece"""

    def __init__(self):
        """Initialize piece attributes"""
        super().__init__()
        self.display = 'P'

    def check_position(self, board):
        """Returns '1' if position is valid."""
        
        possible_positions = []
        # print(self.get_position())
        row = self.get_position()[0]
        col = self.get_position()[1]
        board_pos = board.board[row][col]
        

        # Check top
        row = self.get_position()[0] - 1
        board_pos = board.board[row][col]

        if isinstance(board_pos['piece'], Empty):
            possible_positions.append(board_pos)

        # Check top x 2
        row = self.get_position()[0] - 2
        board_pos = board.board[row][col]

        if isinstance(board_pos['piece'], Empty):
            possible_positions.append(board_pos)

        return possible_positions
        # square = board_pos['piece']
        
        # # Check if there is a piece on the square
        # if(not isinstance(square, Empty)):
        #     square = board_pos['piece']['piece']
        
        # print(self.get_position())
        # print(square.get_position())

        # # Moving piece is white
        # if(self.get_color() == 'white'):
        #     # Cannot move backwards
        #     if(self.get_position()[0] < square.get_position()[0]):
        #         return 0
        #     # Move forward 1 square
        #     if square.get_position()[0] == self.get_position()[0] - 1 and isinstance(square, Empty):
        #         print(square)
        #         return 1