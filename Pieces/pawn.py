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

        for count in range(0, 2):
            # Reset row and col
            row = self.get_position()[0]
            col = self.get_position()[1]

            # Check top
            if count == 0:
                row = row - 1
            # Check top x 2
            elif count == 1:
                row = row - 2

            try:
                board_pos = board.board[row][col]

                if isinstance(board_pos['piece'], Empty):
                    possible_positions.append(board_pos)
            except:
                continue

        return possible_positions