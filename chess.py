from Pieces.empty import Empty
import pygame
from pygame.constants import KEYDOWN, QUIT
from board import Board
from player import Player


# Create players and board
p1 = Player('Player 1')
p2 = Player('Player 2')
board = Board()

turn_order = []
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

# GAME
pygame.init()
pygame.display.set_caption('Chess')
icon = pygame.image.load('Sprites/king_black.png')
pygame.display.set_icon(icon)
size = 650, 650
screen = pygame.display.set_mode(size)

# Text
white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 20)
text_turn = ''
text_total_turns = ''
total_turns = 0

# Display 1st turn
if p1.get_piece_color() == 'white':
    text_turn = font.render(f'Turn: {p1.get_name()} ({p1.get_piece_color().title()})', True, white, black)
else:
    text_turn = font.render(f'Turn: {p2.get_name()} ({p2.get_piece_color().title()})', True, white, black)

text_total_turns = font.render(f'Total turns: {total_turns}', True, white, black)

# board.draw(screen, text_turn, text_total_turns)
board.draw_pieces(screen, text_turn, text_total_turns)

running = True
last_clicked = None
temp_clicked = None
possible_pos = []
turn = turn_order[0]

# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # W.I.P.: Turns
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and running:
            clicked_pos = pygame.mouse.get_pos()
            for row in board.board:
                for p in row:
                    # No piece has been selected
                    if last_clicked == None:
                        if p['rect_pos'].collidepoint(clicked_pos) and isinstance(p['piece'], Empty):
                            print('Empty')
                            break
                        if p['rect_pos'].collidepoint(clicked_pos) and p['piece']['piece'].can_move:
                            last_clicked = p['piece']
                            possible_pos = last_clicked['piece'].check_position(board)
                            # print(possible_pos)
                        if p['rect_pos'].collidepoint(clicked_pos):
                            if not isinstance(p['piece'], Empty):
                                print(f"{p['piece']['piece']}, can_move: {p['piece']['piece'].can_move}, color: {p['piece']['piece'].get_color()}")

                    # Piece has been selected
                    elif temp_clicked == None:
                        if clicked_pos != p['rect_pos'].collidepoint(clicked_pos):
                            if p['rect_pos'].collidepoint(clicked_pos):
                                temp_clicked = p

                            # Clicked on possible position
                            if temp_clicked in possible_pos:
                                board.move_piece(turn, last_clicked, temp_clicked, p1, p2)
                                board.update(screen, text_turn, text_total_turns)

                                # Check if piece can be promoted
                                board.check_piece_promotion(last_clicked, p1, p2, screen, text_turn, text_total_turns, 0, 'white')
                                board.check_piece_promotion(last_clicked, p1, p2, screen, text_turn, text_total_turns, board.rows - 1, 'black')

                                temp_clicked = None
                                last_clicked = None
                                

                            # Clicked on non-possible position
                            else:
                                clicked_pos = pygame.mouse.get_pos()
                                if p['rect_pos'].collidepoint(clicked_pos) and not isinstance(p['piece'], Empty):
                                    if p['piece']['piece'].can_move:
                                        last_clicked = p['piece']
                                        possible_pos = last_clicked['piece'].check_position(board)
                                temp_clicked = None
                                


  
    pygame.display.update()

pygame.quit()

#     for player in turn_order:
#         while True:
#             piece_to_move = input("Enter coordinates of piece you wish to move: ")
# print(p1.pieces[0]['piece'].get_position())
# print(p1.pieces[0]['piece'].check_position(board, (5, 0)))
