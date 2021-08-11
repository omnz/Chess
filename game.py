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
        board.setup(p2, p1)
        p2.turn()
        
        turn_order.append(p2)
        turn_order.append(p1)