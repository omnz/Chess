import pygame
from player import Player
from Pieces.pawn import Pawn
from Pieces.rook import Rook
from Pieces.king import King
from Pieces.queen import Queen
from Pieces.empty import Empty
import pygame

class Board:
    """Chess board model"""
    
    def __init__(self):
        """Initialize board attributes"""
        self.rows = 8
        self.cols = 8
        self.board = [[0]*self.cols for _ in range(0, self.rows)]
        self.board_colors = [[0]*self.cols for _ in range(0, self.rows)]
    
    def setup(self, white, black):
        """Setup the initial board state"""
        empty_rows = [2, 3, 4, 5]

        # Board colors
        alternate = False
        for x in range(0, self.rows):
            for y in range(0, self.cols):
                if alternate == True:
                    self.board[x][y] = {'color': pygame.image.load('Sprites/white.png'), 'piece': 0}
                    alternate = not alternate
                else:
                    self.board[x][y] = {'color': pygame.image.load('Sprites/black.png'), 'piece': 0}
                    alternate = not alternate
            alternate = not alternate
        
        # Board pieces
        for x in range(0, self.rows):
            # Black pieces - Back row
            if x == 0:
                middle_piece = (int)(len(black.pieces)/2)

                for y in range(0, self.cols):
                    self.board[x][y]['piece'] = black.pieces[middle_piece]
                    self.board[x][y]['piece']['piece'].set_position(x, y)
                    self.board[x][y]['piece']['piece'].set_color(black.get_piece_color())
                    middle_piece += 1
            
            # Black pieces - Front row
            if x == 1:
                for y in range(0, self.cols):
                    self.board[x][y]['piece'] = black.pieces[y]
                    self.board[x][y]['piece']['piece'].set_position(x, y)
                    self.board[x][y]['piece']['piece'].set_color(black.get_piece_color())
            
            # White pieces - Front row
            if x == 6:
                for y in range(0, self.cols):
                    self.board[x][y]['piece'] = white.pieces[y]
                    self.board[x][y]['piece']['piece'].set_position(x, y)
                    self.board[x][y]['piece']['piece'].set_color(white.get_piece_color())

            # White pieces - Back row
            if x == 7:
                middle_piece = (int)(len(white.pieces)/2)

                for y in range(0, self.cols):
                    self.board[x][y]['piece'] = white.pieces[middle_piece]
                    self.board[x][y]['piece']['piece'].set_position(x, y)
                    self.board[x][y]['piece']['piece'].set_color(white.get_piece_color())
                    middle_piece += 1
            if x in empty_rows:
                for y in range(0, self.cols):
                    self.board[x][y]['piece'] = Empty()
                    self.board[x][y]['piece'].set_position(x, y)
    
    def move_piece(self, player, last_clicked, new_click, p1, p2):
        """Move a piece and update relevant information"""

        last_clicked = last_clicked['piece']
        temp_pos = last_clicked['rect_pos']
        last_clicked['rect_pos'].update(new_click['rect_pos'])
        new_click['rect_pos'].update(temp_pos)

        last_position_x = last_clicked['piece'].get_position()[0]
        last_position_y = last_clicked['piece'].get_position()[1]
        new_position_x = 0
        new_position_y = 0
        new_piece = None

        # Check if pawn, rook, or king have moved
        if isinstance(last_clicked['piece'], Pawn) or isinstance(last_clicked['piece'], Rook):
            last_clicked['piece'].has_moved = True
        
        elif isinstance(last_clicked['piece'], King) and not last_clicked['piece'].has_moved:
            if isinstance(new_click['piece'], Empty):
                # Move right
                if new_click['piece'].get_position() == (last_position_x, last_position_y + 2):
                    self.move_piece(player, self.board[last_position_x][last_position_y + 3]['piece'], self.board[last_position_x][last_position_y + 1], p1, p2)
                # Move left
                elif new_click['piece'].get_position() == (last_position_x, last_position_y - 2):
                    self.move_piece(player, self.board[last_position_x][last_position_y - 4]['piece'], self.board[last_position_x][last_position_y - 1], p1, p2)
                
                last_clicked['piece'].has_moved = True
                    

        if isinstance(new_click['piece'], Empty):
            new_position_x = new_click['piece'].get_position()[0]
            new_position_y = new_click['piece'].get_position()[1]
            new_piece = new_click['piece']
        else:
            new_position_x = new_click['piece']['piece'].get_position()[0]
            new_position_y = new_click['piece']['piece'].get_position()[1]
            new_piece = new_click['piece']['piece']
        
        # Change position of object
        # temp_pos = last_clicked['piece'].get_position()
        last_clicked['piece'].set_position(new_position_x, new_position_y)
        new_piece.set_position(last_position_x, last_position_y)

        # Change square color
        temp_color = self.board[new_position_x][new_position_y]['color']
        self.board[new_position_x][new_position_y]['color'] = self.board[last_position_x][last_position_y]['color']
        self.board[last_position_x][last_position_y]['color'] = temp_color

        # Change position in board array
        temp_pos = self.board[last_position_x][last_position_y]
        self.board[last_position_x][last_position_y] = self.board[new_position_x][new_position_y]
        self.board[new_position_x][new_position_y] = temp_pos

        # Delete piece and replace with Empty
        if not isinstance(new_click['piece'], Empty):
            scrapped_piece = self.board[last_position_x][last_position_y]['piece']

            # Remove from player's pieces list
            if player.get_name() == 'Player 1':
                # p2.print_piece_index()
                # print(scrapped_piece['piece'].get_index())
                p2.pieces.pop(scrapped_piece['piece'].get_index())
                # p2.print_piece_index()
                p2.set_indexes()
                # p2.print_piece_index()
            else:
                p1.pieces.pop(scrapped_piece['piece'].get_index())
                p1.set_indexes()
            
            # Remove piece from board
            self.board[last_position_x][last_position_y]['piece'] = Empty()
            self.board[last_position_x][last_position_y]['piece'].set_position(last_position_x, last_position_y)
    
    def draw_board(self, screen, current_player, text_details):
        """Draw the chess board"""
        offset = 10
        padding = 60
        x = padding + offset * 2
        y = padding + offset * 3

        # Display 1st turn
        # if p1.get_piece_color() == 'white':
        text_details['text_turn'] = text_details['font'].render(f'Turn: {current_player.get_name()} ({current_player.get_piece_color().title()})', True, text_details['white'], text_details['black'])
        # else:
        #     text_details['text_turn'] = text_details['font'].render(f'Turn: {p2.get_name()} ({p2.get_piece_color().title()})', True, text_details['white'], text_details['black'])

        text_details['text_total_turns'] = text_details['font'].render(f"Total turns: {text_details['total_turns']}", True, text_details['white'], text_details['black'])

        # Display text
        screen.fill((0, 0, 0))
        screen.blit(text_details['text_turn'], (offset * 5, offset))
        screen.blit(text_details['text_total_turns'], (450, offset))
        pygame.display.update()

        # Draw the board
        for row in self.board:
            for n in row:
                square = n['color'].convert()
                n['rect_pos'] = square.get_rect()
                n['rect_pos'].center = (x, y)
                screen.blit(square, n['rect_pos'])
                x += 70
            y += 70
            x = padding + offset * 2
        pygame.display.update()

    def draw_pieces(self, screen, current_player, text_details):
        """Draw the pieces in their initial positions"""
        offset = 10
        padding = 60
        x = padding + offset * 2
        y = padding + offset * 3

        self.draw_board(screen, current_player, text_details)
        # Draw the pieces
        for row in self.board:
            for p in row:
                if not isinstance(p['piece'], Empty):
                    piece = p['piece']['img'].convert_alpha()
                    p['piece']['rect_pos'] = piece.get_rect()
                    p['piece']['rect_pos'].center = (x, y)
                    screen.blit(piece, p['piece']['rect_pos'])
                x += 70
            y += 70
            x = padding + offset * 2
        pygame.display.update()        
    
    def update(self, screen, current_player, text_details):
        """Update the board and pieces"""
        self.draw_board(screen, current_player, text_details)

        for row in self.board:
            for p in row:
                if not isinstance(p['piece'], Empty):
                    piece = p['piece']['img'].convert_alpha()
                    screen.blit(piece, p['piece']['rect_pos'])
        
        pygame.display.update()
    
    def check_piece_promotion(self, piece, current_player, screen, text_details, row, p1):
        """Check if any piece in row can be promoted"""

        if isinstance(piece['piece']['piece'], Pawn):
            row = piece['piece']['piece'].get_position()[0]
            col = piece['piece']['piece'].get_position()[1]
            print(current_player)
            print(p1)

            if current_player.get_piece_color() == 'white':
                # Player 1 is white
                if current_player == p1:
                    if row == 0:
                        current_player.promote_piece(self, piece, row, col)
                        self.update(screen, current_player, text_details)
                # Player 2 is white
                else:
                    print(f"Row: {row}")
                    if row == self.rows - 1:
                        print(f"Row: {row}")
                        current_player.promote_piece(self, piece, row, col)
                        self.update(screen, current_player, text_details)
            else:
                # Player 1 is black
                if current_player == p1:
                    if row == 0:
                        current_player.promote_piece(self, piece, row, col)
                        self.update(screen, current_player, text_details)
                # Player 2 is black
                else:
                    if row == self.rows - 1:
                        current_player.promote_piece(self, piece, row, col)
                        self.update(screen, current_player, text_details)
                    
            

        # col = 0
        # for piece in self.board[row]:
        #     if not isinstance(piece['piece'], Empty):
        #         if isinstance(piece['piece']['piece'], Pawn):
        #             if piece['piece']['piece'].get_color() == color:
        #                 if p1.get_piece_color() == color:
        #                     p1.promote_piece(self, piece, row, col)
        #                 elif p2.get_piece_color() == color:
        #                     p2.promote_piece(self, piece, row, col)
        #                 self.update(screen, p1, p2, text_details)
        #     col += 1