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
pygame.font.init()
pygame.display.set_caption('Chess')
icon = pygame.image.load('Sprites/king_black.png')
pygame.display.set_icon(icon)
size = 650, 650
black = 0, 0, 0
screen = pygame.display.set_mode(size)
text_player = pygame.image.load('Sprites/text_player.png')
text_p1 = pygame.image.load('Sprites/one.png')
text_p2 = pygame.image.load('Sprites/two.png')

padding = (5, 5)
white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render(f'Player: 1 ({p1.get_piece_color().title()})', True, white, black)
screen.blit(text, padding)
pygame.display.update()


padding = 65
x = padding
y = padding

# Draw the board
for row in board.board:
    for n in row:
        square = n['color'].convert()
        screen.blit(square, (x, y))
        x += 65
    y += 65
    x = padding
pygame.display.update()

x = padding
y = padding

# Draw the pieces
for row in board.board:
    for p in row:
        if p['piece'] != 0:
            piece = p['piece']['img'].convert_alpha()
            screen.blit(piece, (x, y))
        x += 65
    y += 65
    x = padding
pygame.display.update()

running = True

# Game Loop
while running:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            running = False
    
    # W.I.P.: Turns
    pygame.display.update()

pygame.quit()

#     for player in turn_order:
#         while True:
#             piece_to_move = input("Enter coordinates of piece you wish to move: ")
