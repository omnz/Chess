import pygame, sys

from Pieces.pawn import Pawn
from Pieces.rook import Rook
from Pieces.bishop import Bishop
from Pieces.king import King
from Pieces.knight import Knight
from Pieces.queen import Queen

class Player:
    def __init__(self, name):
        """Initialize player's attributes and pieces"""
        self.name = name
        self.pieces = []
        self.is_turn = False
        self.piece_color = None
        self.winner = False
    
    def set_name(self, name):
        """Set the player's name"""
        self.name = name
    
    def get_name(self):
        """Return the player's name"""
        return self.name

    def set_piece_color(self, color):
        """Set the player's name"""
        self.piece_color = color
    
    def get_piece_color(self):
        """Return the player's piece color"""
        return self.piece_color

    def turn(self):
        """Switch is_turn to True/False"""
        self.is_turn = not self.is_turn

    def build_pieces(self, color):
        """Build list of all pieces"""
        for n in range(0, 8):
            self.pieces.append({'piece': Pawn(), 'img': pygame.image.load(f'Sprites/pawn_{color}.png')})

        otherPieces = [
            {'piece': Rook(), 'img': pygame.image.load(f'Sprites/rook_{color}.png'),},
            {'piece': Knight(), 'img': pygame.image.load(f'Sprites/knight_{color}.png')},
            {'piece': Bishop(), 'img': pygame.image.load(f'Sprites/bishop_{color}.png')},
            {'piece': Queen(), 'img': pygame.image.load(f'Sprites/queen_{color}.png')}, 
            {'piece': King(), 'img': pygame.image.load(f'Sprites/king_{color}.png')},
            {'piece': Bishop(), 'img': pygame.image.load(f'Sprites/bishop_{color}.png')},
            {'piece': Knight(), 'img': pygame.image.load(f'Sprites/knight_{color}.png')},
            {'piece': Rook(), 'img': pygame.image.load(f'Sprites/rook_{color}.png')}]

        for p in otherPieces:
            self.pieces.append(p)

        self.set_indexes()

    def set_indexes(self):
        """Set indexes for place in 'pieces' list"""
        count = 0
        for piece in self.pieces:
            piece['piece'].set_index(count)
            count += 1

    def print_pieces(self):
        """Print all of the player's pieces"""
        for piece in self.pieces:
            print(piece)
    
    def promote_piece(self, board, piece, row, col, screen, text_details, size):
        """Promote piece to Queen"""
        surface = pygame.Surface(size, pygame.SRCALPHA)
        surface.convert_alpha()
        surface.fill((0, 0, 0, 180))
        screen.blit(surface, (0, 0))

        x = size[0] / 2
        y = size[1] / 2
        color = (185, 153, 118)

        promotion_text = text_details['font'].render("choose promotion:".title(), True, text_details['white'])
        promotion_rect = promotion_text.get_rect(center=(x, y - 100))

        queen = pygame.image.load(f'Sprites/queen_{self.get_piece_color()}.png')
        queen_rect = queen.get_rect(center=(x - 70, y))
        knight = pygame.image.load(f'Sprites/knight_{self.get_piece_color()}.png')
        knight_rect = knight.get_rect(center=(x + 70, y))
        rook = pygame.image.load(f'Sprites/rook_{self.get_piece_color()}.png')
        rook_rect = rook.get_rect(center=(x - 70, y + 100))
        bishop = pygame.image.load(f'Sprites/bishop_{self.get_piece_color()}.png')
        bishop_rect = bishop.get_rect(center=(x + 70, y + 100))

        pygame.draw.rect(screen, color, (x - 125, y - 70, 250, 250))
        screen.blit(promotion_text, promotion_rect)
        screen.blit(queen, queen_rect)
        screen.blit(knight, knight_rect)
        screen.blit(rook, rook_rect)
        screen.blit(bishop, bishop_rect)
        pygame.display.update()

        pick_promotion = True

        # Get player 1's choice of color, then set both player's
        while pick_promotion:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_click = pygame.mouse.get_pos()

                    if queen_rect.collidepoint(mouse_click):
                        index = piece['piece']['piece'].get_index()
                        self.pieces[index]['piece'] = Queen()
                        self.pieces[index]['piece'].set_color(self.get_piece_color())
                        self.pieces[index]['piece'].set_position(row, col)
                        self.pieces[index]['piece'].set_index(index)
                        self.pieces[index]['piece'].can_move = True
                        board.board[row][col]['piece']['img'] = queen
                        pick_promotion = False
                        break

                    elif knight_rect.collidepoint(mouse_click):
                        index = piece['piece']['piece'].get_index()
                        self.pieces[index]['piece'] = Knight()
                        self.pieces[index]['piece'].set_color(self.get_piece_color())
                        self.pieces[index]['piece'].set_position(row, col)
                        self.pieces[index]['piece'].set_index(index)
                        self.pieces[index]['piece'].can_move = True
                        board.board[row][col]['piece']['img'] = knight
                        pick_promotion = False
                        break

                    elif rook_rect.collidepoint(mouse_click):
                        index = piece['piece']['piece'].get_index()
                        self.pieces[index]['piece'] = Rook()
                        self.pieces[index]['piece'].set_color(self.get_piece_color())
                        self.pieces[index]['piece'].set_position(row, col)
                        self.pieces[index]['piece'].set_index(index)
                        self.pieces[index]['piece'].can_move = True
                        board.board[row][col]['piece']['img'] = rook
                        pick_promotion = False
                        break

                    elif bishop_rect.collidepoint(mouse_click):
                        index = piece['piece']['piece'].get_index()
                        self.pieces[index]['piece'] = Bishop()
                        self.pieces[index]['piece'].set_color(self.get_piece_color())
                        self.pieces[index]['piece'].set_position(row, col)
                        self.pieces[index]['piece'].set_index(index)
                        self.pieces[index]['piece'].can_move = True
                        board.board[row][col]['piece']['img'] = bishop
                        pick_promotion = False
                        break
        
        
    def print_piece_index(self):
        """Print all of a players pieces with their corresponding index"""
        for p in self.pieces:
            print(f"{p['piece']}, {p['piece'].get_index()}")
        print()

    def set_winner(self):
        self.winner = True