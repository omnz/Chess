from Pieces.piece import Piece
from Pieces.empty import Empty
from Pieces.rook import Rook


class King(Piece):
    """King piece"""

    def __init__(self):
        """Initialize piece attributes"""
        super().__init__()
        self.display = 'K'
        self.has_moved = False
    
    def check_position(self, board, player, p1):
        """Returns '1' if position is valid."""
        
        possible_positions = []

        for count in range(0, 8):
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

            # Check top-left
            elif count == 4:
                row = row - 1
                col = col - 1

            # Check top-right
            elif count == 5:
                row = row - 1
                col = col + 1

            # Check bottom-left
            elif count == 6:
                row = row + 1
                col = col - 1

            # Check bottom-right
            elif count == 7:
                row = row + 1
                col = col + 1

            try:
                if row >= 0:
                    board_pos = board.board[row][col]

                    # Check if new position is empty or held by enemy
                    if isinstance(board_pos['piece'], Empty) or board_pos['piece']['piece'].get_color() != self.get_color():
                        possible_positions.append(board_pos)
            except:
                continue

        # King & Rook swap
        if not self.has_moved:
            row = self.get_position()[0]
            col = self.get_position()[1]
            board_pos = board.board[row]

            # Right
            if isinstance(board_pos[col + 1]['piece'], Empty) and isinstance(board_pos[col + 2]['piece'], Empty):
                if isinstance(board_pos[col + 3]['piece']['piece'], Rook) and board_pos[col + 3]['piece']['piece'].has_moved == False:
                    col = col + 2
                    board_pos = board.board[row][col]
                    possible_positions.append(board_pos)

            # Left
            board_pos = board.board[row]
            if isinstance(board_pos[col - 1]['piece'], Empty) and isinstance(board_pos[col - 2]['piece'], Empty) and isinstance(board_pos[col - 3]['piece'], Empty):
                if isinstance(board_pos[col - 4]['piece']['piece'], Rook) and board_pos[col - 4]['piece']['piece'].has_moved == False:
                    col = col - 2
                    board_pos = board.board[row][col]
                    possible_positions.append(board_pos)

        return possible_positions