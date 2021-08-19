import pygame
from Pieces.empty import Empty
from Pieces.pawn import Pawn
from Pieces.king import King

def get_player_colors(p1, p2):
    """Ask player 1 for choice of piece color"""
    while True:
        color = input(f"{p1.get_name()}, which color piece are you (white/black)? ")
        if color[0].lower() == 'w':
            p1.set_piece_color('white')
            p2.set_piece_color('black')

            print(f"{p1.get_name()}, your piece color is {p1.get_piece_color()}.")
            print(f"{p2.get_name()}, your piece color is {p2.get_piece_color()}.")
            break
        elif color[0].lower() == 'b':
            p1.set_piece_color('black')
            p2.set_piece_color('white')

            print(f"{p1.get_name()}, your piece color is {p1.get_piece_color()}.")
            print(f"{p2.get_name()}, your piece color is {p2.get_piece_color()}.")
            break
        else:
            print("Error: Did not enter white or black!\n")

    print()

def setup(board, p1, p2, turn_order):
    """Set up the board and turn order"""
    if(p1.get_piece_color() == 'white'):
        p1.build_pieces('white')
        p2.build_pieces('black')
        board.setup(p1, p2)
        p1.turn()
        
        turn_order.append(p1)
        turn_order.append(p2)
        
    else:
        p1.build_pieces('black')
        p2.build_pieces('white')
        board.setup(p1, p2)
        p2.turn()
        
        turn_order.append(p2)
        turn_order.append(p1)

def show_possible_moves(possible_pos, screen, surface, board, player, p1):
    """Show all of a piece's possible moves"""
    surface.fill((0, 0, 0, 0))
    for p in possible_pos:
        surface.fill((0, 0, 0, 0))
        x = p['rect_pos'][0]
        y = p['rect_pos'][1]

        if isinstance(p['piece'], Empty):
            row = p['piece'].get_position()[0]
            col = p['piece'].get_position()[1]

            red = False
            adjust = 0
        
            if player.get_piece_color() == p1.get_piece_color():
                adjust = 1
            else:
                adjust = -1
            
            # Color: Red
            try:
                if not isinstance(board.board[row - 1 * adjust][col]['piece'], Empty):
                    if isinstance(board.board[row - 1 * adjust][col]['piece']['piece'], Pawn):
                        if board.board[row - 1 * adjust][col]['piece']['piece'].en_passant and board.board[row][col] in possible_pos:
                            print(p['piece'].get_position())
                            pygame.draw.rect(surface, (141, 49, 35, 180), (x, y, 64, 64))
                            red = True
            except:
                pass

            if red == False:
                try:
                    if not isinstance(board.board[row + 1 * adjust][col]['piece'], Empty):
                        if isinstance(board.board[row + 1 * adjust][col]['piece']['piece'], Pawn):
                            if board.board[row + 1 * adjust][col]['piece']['piece'].en_passant and board.board[row][col] in possible_pos:
                                pygame.draw.rect(surface, (141, 49, 35, 180), (x, y, 64, 64))
                                red = True
                except:
                    pass

            # Color: Brown
            if red == False:
                pygame.draw.rect(surface, (102, 66, 41, 255), (x, y, 64, 64))
        else:
            # Color: Red
            pygame.draw.rect(surface, (141, 49, 35, 180), (x, y, 64, 64))
            
        screen.blit(surface, (0, 0))

def empty_list(clicks):
    """Empty the given list"""
    while clicks:
        clicks.pop()

def next_turn(current_player, turn_order, p1, p2):
    """Flip current_player to next player"""
    p1.turn()
    p2.turn()

    if current_player == turn_order[0]:
        current_player = turn_order[1]
    else:
        current_player = turn_order[0]

    return current_player

def remove_en_passant(p1, p2):
    """Remove en passant if move not utilized"""
    for p in p1.pieces:
        if isinstance(p['piece'], Pawn):
            if p['piece'].en_passant and p['counter'] == 0:
                p['counter'] += 1
            elif p['piece'].en_passant and p['counter'] == 1:
                p['piece'].not_en_passant()

    for p in p2.pieces:
        if isinstance(p['piece'], Pawn):
            if p['piece'].en_passant and p['counter'] == 0:
                p['counter'] += 1
            elif p['piece'].en_passant and p['counter'] == 1:
                p['piece'].not_en_passant()

def check_mate(player, p1, p2):
    """Check for game over"""
    piece = None

    # Get King
    for p in player.pieces:
        if isinstance(p['piece'], King):
            piece = p['piece']
            break

    if piece == None:
        if player == p1:
            p2.set_winner()
        else:
            p1.set_winner()
        return True
    else:
        return False

def game_over(player, p1, p2, text_details, screen, size, game_draw):
    """Display game over screen"""
    surface = pygame.Surface(size, pygame.SRCALPHA)
    surface.convert_alpha()
    surface.fill((0, 0, 0, 180))
    screen.blit(surface, (0, 0))
    winner = None
    text_details['font'] = pygame.font.Font('freesansbold.ttf', 30)

    if p1.winner:
        winner = text_details['font'].render(f"{p1.get_name()} Wins!!!", True, text_details['white'])
    elif p2.winner:
        winner = text_details['font'].render(f"{p2.get_name()} Wins!!!", True, text_details['white'])
    elif game_draw:
        winner = text_details['font'].render("Draw!", True, text_details['white'])
    
    winner_rect = winner.get_rect(center=(size[0] / 2, size[1] / 2))
    screen.blit(winner, winner_rect)