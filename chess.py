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
surface = pygame.Surface(size, pygame.SRCALPHA)
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
possible_pos = []
current_player = turn_order[0]
clicks = []
# print(board.board[1][5]['piece']['piece'].can_move)
print(current_player.get_piece_color(), current_player.is_turn)

# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # W.I.P.: Turns
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and running:
            mouse_click = pygame.mouse.get_pos()
                
            if len(clicks) < 2:
                for row in board.board:
                    for p in row:
                        clicked_square = p['rect_pos'].collidepoint(mouse_click)

                        # If clicked square is empty
                        if clicked_square and isinstance(p['piece'], Empty):
                            print('Empty')
                            possible_pos = p['piece'].check_position(board, current_player, p1)
                            game.show_possible_moves(possible_pos, screen, surface)
                            board.update(screen, p1, p2, text_details)

                            # Check if a piece has already been selected
                            if len(clicks) == 1:
                                last_clicked = p
                                
                                # Check if empty space is a plausible move
                                if last_clicked in clicks[0]['possible_pos']:
                                    clicks.append({'piece': last_clicked})
                                else:
                                    clicks.pop()
                                break

                        # If clicked square is NOT empty
                        elif clicked_square and not isinstance(p['piece'], Empty):
                            # print(f"{p['piece']['piece']}, can_move: {p['piece']['piece'].can_move}, color: {p['piece']['piece'].get_color()}")
                            print(f"{p['piece']['piece']}, color: {p['piece']['piece'].get_color()}")

                            # Select one of your pieces
                            if current_player.is_turn and p['piece']['piece'].get_color() == current_player.get_piece_color():
                            # if p['piece']['piece'].can_move:
                                last_clicked = p
                                print("Hello")

                                # Select first piece
                                if len(clicks) == 0:
                                    possible_pos = last_clicked['piece']['piece'].check_position(board, current_player, p1)
                                    board.update(screen, p1, p2, text_details)
                                    game.show_possible_moves(possible_pos, screen, surface)
                                    clicks.append({'piece': last_clicked, 'possible_pos': possible_pos})
                                    break

                                # Select a different/same piece
                                else:
                                    possible_pos = last_clicked['piece']['piece'].check_position(board, current_player, p1)
                                    board.update(screen, p1, p2, text_details)
                                    game.show_possible_moves(possible_pos, screen, surface)
                                    clicks.pop()
                                    clicks.append({'piece': last_clicked, 'possible_pos': possible_pos})
                                    break
                            
                            # Select enemy piece
                            else:
                                last_clicked = p
                                if last_clicked in clicks[0]['possible_pos']:
                                    clicks.append({'piece': last_clicked})
                                    break
                                else:
                                    game.empty_list(clicks)

            # Move piece
            if len(clicks) == 2:
                board.move_piece(current_player, clicks[0]['piece'], clicks[1]['piece'], p1, p2)
                board.update(screen, p1, p2, text_details)

                # Check if piece can be promoted
                board.check_piece_promotion(clicks[0], p1, p2, screen, text_details, 0, 'white')
                board.check_piece_promotion(clicks[0], p1, p2, screen, text_details, board.rows - 1, 'black')

                game.empty_list(clicks)
                current_player = game.next_turn(current_player, turn_order, p1, p2)
                # print(current_player.get_piece_color(), current_player.is_turn)                       
                                
    pygame.display.update()

pygame.quit()
