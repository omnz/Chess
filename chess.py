from board import Board
from player import Player

# Create players and board
p1 = Player('Player 1')
p2 = Player('Player 2')
board = Board()

turn_order = []
game_over = False
winner = ''

# Ask first player for piece color
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

# Setup the board
if(p1.get_piece_color() == 'white'):
    board.setup(p1, p2)
    p1.turn()

    turn_order.append(p1)
    turn_order.append(p2)
else:
    board.setup(p2, p1)
    p2.turn()
    
    turn_order.append(p2)
    turn_order.append(p1)

board.display()
# print(p1.pieces[0].can_move)
# print(p2.pieces[0].can_move)

# Game Loop
# while game_over == False:
#     for player in turn_order:
#         while True:
#             piece_to_move = input("Enter coordinates of piece you wish to move: ")
