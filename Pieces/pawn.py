from Pieces.piece import Piece
from Pieces.empty import Empty


class Pawn(Piece):
    """Pawn piece"""

    def __init__(self):
        """Initialize piece attributes"""
        super().__init__()
        self.display = 'P'
        self.has_moved = False
        self.en_passant = False

    def check_position(self, board, player, p1):
        """Returns '1' if position is valid."""
        
        possible_positions = []
        adjust = 0
        
        if player.get_piece_color() == p1.get_piece_color():
            adjust = 1
        else:
            adjust = -1

        for count in range(0, 6):
            # Reset row and col
            row = self.get_position()[0]
            col = self.get_position()[1]

            # Check top
            if count == 0:
                if isinstance(board.board[row - 1 * adjust][col]['piece'], Empty):
                    row = row - 1 * adjust
            # Check top x 2
            elif count == 1:
                if self.has_moved == False:
                    if isinstance(board.board[row - 2 * adjust][col]['piece'], Empty) and isinstance(board.board[row - 1 * adjust][col]['piece'], Empty):
                        row = row - 2 * adjust
                else:
                    continue
            # Diagonal left
            elif count == 2:
                try:
                    # Check if new position is NOT empty and is held by enemy
                    if not isinstance(board.board[row - 1 * adjust][col - 1]['piece'], Empty):
                        if board.board[row - 1 * adjust][col - 1]['piece']['piece'].get_color() != self.get_color():
                            row = row - 1 * adjust
                            col = col - 1
                    else:
                        continue
                except:
                    continue
            elif count == 3:
                try:
                    # Check if new position is empty and is en passant
                    if isinstance(board.board[row - 1 * adjust][col - 1 * adjust]['piece'], Empty):
                        if board.board[row][col - 1  * adjust]['piece']['piece'].en_passant:
                            row = row - 1 * adjust
                            col = col - 1 * adjust
                    else:
                        continue
                except:
                    continue
            # Diagonal right
            elif count == 4:
                try:
                    # Check if new position is NOT empty and is held by enemy
                    if not isinstance(board.board[row - 1 * adjust][col + 1]['piece'], Empty):
                        if board.board[row - 1 * adjust][col + 1]['piece']['piece'].get_color() != self.get_color():
                            row = row - 1 * adjust
                            col = col + 1
                    else:
                        continue
                except:
                    continue
            elif count == 5:
                try:
                    # Check if new position is empty and is en passant
                    if isinstance(board.board[row - 1 * adjust][col + 1 * adjust]['piece'], Empty):
                        if board.board[row][col + 1 * adjust]['piece']['piece'].en_passant:
                            row = row - 1 * adjust
                            col = col + 1 * adjust
                    else:
                        continue
                except:
                    continue

            # Try position on board
            try:
                if row != 0 and col != -1:
                    if row != self.get_position()[0] or col != self.get_position()[1]:
                        board_pos = board.board[row][col]
                        possible_positions.append(board_pos)
            except:
                continue

        return possible_positions
    
    def not_en_passant(self):
        self.en_passant = False