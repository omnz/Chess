import pygame
from player import Player
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
    
    def move_piece(self, screen, last_clicked, new_click):
        """Move a piece and update relevant information"""
        # print(last_clicked)
        # print(new_click)
        temp_pos = last_clicked['rect_pos']
        last_clicked['rect_pos'].update(new_click['rect_pos'])
        new_click['rect_pos'].update(temp_pos)

        # last_clicked['rect_pos'].move(new_click['rect_pos'][0], new_click['rect_pos'][1])
        # new_click['rect_pos'].move(temp_pos[0], temp_pos[1])

        # Change position of object
        temp_pos = last_clicked['piece'].get_position()
        last_clicked['piece'].set_position(new_click['piece'].get_position()[0], new_click['piece'].get_position()[1])
        new_click['piece'].set_position(temp_pos[0], temp_pos[1])

        # Change square color
        temp_color = self.board[new_click['piece'].get_position()[0]][new_click['piece'].get_position()[1]]['color']
        self.board[new_click['piece'].get_position()[0]][new_click['piece'].get_position()[1]]['color'] = self.board[last_clicked['piece'].get_position()[0]][last_clicked['piece'].get_position()[1]]['color']
        self.board[last_clicked['piece'].get_position()[0]][last_clicked['piece'].get_position()[1]]['color'] = temp_color

        # Change position in board array
        temp_pos = self.board[last_clicked['piece'].get_position()[0]][last_clicked['piece'].get_position()[1]]
        self.board[last_clicked['piece'].get_position()[0]][last_clicked['piece'].get_position()[1]] = self.board[new_click['piece'].get_position()[0]][new_click['piece'].get_position()[1]]
        self.board[new_click['piece'].get_position()[0]][new_click['piece'].get_position()[1]] = temp_pos

    
    def draw_board(self, screen, text_turn, text_total_turns):
        """Draw the chess board"""
        offset = 10
        padding = 65
        x = padding
        y = padding + offset

        # Display text
        screen.blit(text_turn, (offset, offset))
        screen.blit(text_total_turns, (475, offset))
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
            x = padding
        pygame.display.update()

    def draw_pieces(self, screen, text_turn, text_total_turns):
        """Draw the pieces in their initial positions"""
        offset = 10
        padding = 65
        x = padding
        y = padding + offset

        self.draw_board(screen, text_turn, text_total_turns)
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
            x = padding
        pygame.display.update()
        
    
    def update(self, screen, text_turn, text_total_turns):
        """Update the board and pieces"""
        self.draw_board(screen, text_turn, text_total_turns)

        for row in self.board:
            for p in row:
                if not isinstance(p['piece'], Empty):
                    piece = p['piece']['img'].convert_alpha()
                    screen.blit(piece, p['piece']['rect_pos'])
        
        pygame.display.update()

        

