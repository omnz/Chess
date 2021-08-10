from Pieces.piece import Piece
from Pieces.empty import Empty


class King(Piece):
    """King piece"""

    def __init__(self):
        """Initialize piece attributes"""
        super().__init__()
        self.display = 'K'
    
    def check_position(self, board):
        """Returns '1' if position is valid."""
        
        possible_positions = []

        for count in range(0, 4):
            # Reset row and col
            row = self.get_position()[0]
            col = self.get_position()[1]

            # Check top
            if count == 0:
                row = row - 1

            # Check right
            elif count == 1:
                col = col + 1

            # Check left
            elif count == 2:
                col = col - 1

            # Check bottom
            elif count == 3:
                row = row + 1

            try:
                board_pos = board.board[row][col]

                if isinstance(board_pos['piece'], Empty):
                    possible_positions.append(board_pos)
            except:
                continue

        return possible_positions