from Pieces.piece import Piece
from Pieces.empty import Empty


class Knight(Piece):
    """Knight piece"""

    def __init__(self):
        """Initialize piece attributes"""
        super().__init__()
        self.display = 'N'
    
    def check_position(self, board):
        """Returns '1' if position is valid."""
        
        possible_positions = []

        for count in range(0, 8):
            # Reset row and col
            row = self.get_position()[0]
            col = self.get_position()[1]

            # Check all possible positions
            if count == 0:
                row = row - 1
                col = col - 2
            elif count == 1:
                row = row - 2
                col = col - 1
            elif count == 2:
                row = row - 2
                col = col + 1
            elif count == 3:
                row = row - 1
                col = col + 2
            elif count == 4:
                row = row + 1
                col = col + 2
            elif count == 5:
                row = row + 2
                col = col + 1
            elif count == 6:
                row = row + 2
                col = col - 1
            elif count == 7:
                row = row + 1
                col = col - 2

            try:
                board_pos = board.board[row][col]

                # Check if new position is empty or held by enemy
                if isinstance(board_pos['piece'], Empty) or board_pos['piece']['piece'].get_color() != self.get_color():
                    possible_positions.append(board_pos)
            except:
                continue

        return possible_positions