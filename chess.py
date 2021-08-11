from Pieces.empty import Empty
import pygame
import game
from pygame.constants import KEYDOWN, QUIT
from board import Board
from player import Player


# Create players and board
p1 = Player('Player 1')
p2 = Player('Player 2')
board = Board()
turn_order = []

game.get_player_colors(p1, p2)
game.setup(board, p1, p2, turn_order)

# GAME
pygame.init()
pygame.display.set_caption('Chess')
icon = pygame.image.load('Sprites/king_black.png')
pygame.display.set_icon(icon)
size = 650, 650
screen = pygame.display.set_mode(size)
text_details = {
    'text_turn': '',
    'text_total_turns': '',
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'font': pygame.font.Font('freesansbold.ttf', 20),
    'total_turns': 0
}

board.draw_pieces(screen, p1, p2, text_details)

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
                                board.update(screen, p1, p2, text_details)

                                # Check if piece can be promoted
                                board.check_piece_promotion(last_clicked, p1, p2, screen, text_details, 0, 'white')
                                board.check_piece_promotion(last_clicked, p1, p2, screen, text_details, board.rows - 1, 'black')

                                temp_clicked = None
                                last_clicked = None
                                
                            # Clicked on non-possible position
                            else:
                                clicked_pos = pygame.mouse.get_pos()

                                # Clicked on a piece
                                if p['rect_pos'].collidepoint(clicked_pos) and not isinstance(p['piece'], Empty):
                                    if p['piece']['piece'].can_move:
                                        last_clicked = p['piece']
                                        possible_pos = last_clicked['piece'].check_position(board)
                                temp_clicked = None
                                
    pygame.display.update()

pygame.quit()
