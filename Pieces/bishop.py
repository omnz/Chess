from Pieces.piece import Piece
from Pieces.empty import Empty


class Bishop(Piece):
    """Bishop piece"""

    def __init__(self):
        """Initialize piece attributes"""
        super().__init__()
        self.display = 'B'
    
    def check_position(self, board):
        """Returns '1' if position is valid."""
        
        possible_positions = []

        for count in range(0, 4):
            # Reset row and col
            row = self.get_position()[0]
            col = self.get_position()[1]

            # Check top-left
            if count == 0:
                while row > 0 and col > 0:
                    row = row - 1
                    col = col - 1
                    
                    try:
                        board_pos = board.board[row][col]

                        # Check if new position is empty or held by enemy
                        if isinstance(board_pos['piece'], Empty):
                            possible_positions.append(board_pos)
                        else:
                            if board_pos['piece']['piece'].get_color() != self.get_color():
                                possible_positions.append(board_pos)
                            break
                    except:
                        continue

            # Check top-right
            elif count == 1:
                while row > 0 and col < board.cols:
                    row = row - 1
                    col = col + 1

                    try:
                        board_pos = board.board[row][col]

                        # Check if new position is empty or held by enemy
                        if isinstance(board_pos['piece'], Empty):
                            possible_positions.append(board_pos)
                        else:
                            if board_pos['piece']['piece'].get_color() != self.get_color():
                                possible_positions.append(board_pos)
                            break
                    except:
                        continue

            # Check bottom-right
            elif count == 2:
                while row < board.rows and col < board.cols:
                    row = row + 1
                    col = col + 1

                    try:
                        board_pos = board.board[row][col]

                        # Check if new position is empty or held by enemy
                        if isinstance(board_pos['piece'], Empty):
                            possible_positions.append(board_pos)
                        else:
                            if board_pos['piece']['piece'].get_color() != self.get_color():
                                possible_positions.append(board_pos)
                            break
                    except:
                        continue

            # Check bottom-left
            elif count == 3:
                while row < board.rows and col > 0:
                    row = row + 1
                    col = col - 1

                    try:
                        board_pos = board.board[row][col]

                        # Check if new position is empty or held by enemy
                        if isinstance(board_pos['piece'], Empty):
                            possible_positions.append(board_pos)
                        else:
                            if board_pos['piece']['piece'].get_color() != self.get_color():
                                possible_positions.append(board_pos)
                            break
                    except:
                        continue

        return possible_positions