from Pieces.piece import Piece
from Pieces.empty import Empty


class Pawn(Piece):
    """Pawn piece"""

    def __init__(self):
        """Initialize piece attributes"""
        super().__init__()
        self.display = 'P'
        self.has_moved = False

    def check_position(self, board):
        """Returns '1' if position is valid."""
        
        possible_positions = []

        for count in range(0, 4):
            # Reset row and col
            row = self.get_position()[0]
            col = self.get_position()[1]

            # Check top
            if count == 0:
                if isinstance(board.board[row - 1][col]['piece'], Empty):
                    row = row - 1
            # Check top x 2
            elif count == 1:
                if self.has_moved == False:
                    if isinstance(board.board[row - 2][col]['piece'], Empty):
                        row = row - 2
                else:
                    continue
            # Diagonal left
            elif count == 2:
                try:
                    # Check if new position is NOT empty and is held by enemy
                    if not isinstance(board.board[row - 1][col - 1]['piece'], Empty):
                        print(board.board[row - 1][col - 1]['piece']['piece'].get_color())
                        if board.board[row - 1][col - 1]['piece']['piece'].get_color() != self.get_color():
                            row = row - 1
                            col = col - 1
                    else:
                        continue
                except:
                    continue
            # Diagonal right
            elif count == 3:
                try:
                    # Check if new position is NOT empty and is held by enemy
                    if not isinstance(board.board[row - 1][col + 1]['piece'], Empty):
                        print(board.board[row - 1][col - 1]['piece']['piece'].get_color())
                        if board.board[row - 1][col + 1]['piece']['piece'].get_color() != self.get_color():
                            row = row - 1
                            col = col + 1
                    else:
                        continue
                except:
                    continue
            try:
                if row != self.get_position()[0] or col != self.get_position()[1]:
                    board_pos = board.board[row][col]
                    possible_positions.append(board_pos)
            except:
                continue

        return possible_positions