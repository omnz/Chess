from Pieces.empty import Empty
import pygame

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

def show_possible_moves(possible_pos, screen, surface):
    surface.fill((0, 0, 0, 0))
    for p in possible_pos:
        # print(p)
        surface.fill((0, 0, 0, 0))
        x = p['rect_pos'][0]
        y = p['rect_pos'][1]

        if isinstance(p['piece'], Empty):
            circle = pygame.draw.rect(surface, (102, 66, 41, 255), (x, y, 64, 64))
        else:
            circle = pygame.draw.rect(surface, (141, 49, 35, 180), (x, y, 64, 64))
        screen.blit(surface, (0, 0))

def empty_list(clicks):
    while clicks:
        clicks.pop()

def next_turn(current_player, turn_order, p1, p2):
    p1.turn()
    p2.turn()

    if current_player == turn_order[0]:
        current_player = turn_order[1]
    else:
        current_player = turn_order[0]

    return current_player