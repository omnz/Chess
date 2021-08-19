import pygame
import game
from pygame.constants import KEYDOWN, QUIT
from board import Board
from player import Player
from Pieces.empty import Empty
from Pieces.pawn import Pawn


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
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 650
size = SCREEN_WIDTH, SCREEN_HEIGHT
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

running = True
game_draw = False
game_over = False
game_over_count = 0
possible_pos = []
current_player = turn_order[0]
clicks = []

board.draw_pieces(screen, current_player, text_details)

# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and running and game_over == False:
            mouse_click = pygame.mouse.get_pos()
                
            if len(clicks) < 2:
                for row in board.board:
                    for p in row:
                        clicked_square = p['rect_pos'].collidepoint(mouse_click)

                        # If clicked square is empty
                        if clicked_square and isinstance(p['piece'], Empty):
                            # print(p['piece'])
                            possible_pos = p['piece'].check_position(board, current_player, p1)
                            game.show_possible_moves(possible_pos, screen, surface, board, current_player, p1)
                            board.update(screen, current_player, text_details)

                            # Check if a piece has already been selected
                            if len(clicks) == 1:
                                last_clicked = p
                                
                                # Check if empty space is a plausible move
                                if last_clicked in clicks[0]['possible_pos']:
                                    clicks.append({'piece': last_clicked})
                                else:
                                    game.empty_list(clicks)
                                break

                        # If clicked square is NOT empty
                        elif clicked_square and not isinstance(p['piece'], Empty):
                            if isinstance(p['piece']['piece'], Pawn):
                                print(f"{p['piece']['piece']}, color: {p['piece']['piece'].get_color()}, en_passant: {p['piece']['piece'].en_passant}")
                            else:
                                print(f"{p['piece']['piece']}, color: {p['piece']['piece'].get_color()}")

                            # Select one of your pieces
                            if current_player.is_turn and p['piece']['piece'].get_color() == current_player.get_piece_color():
                                last_clicked = p

                                # Select first piece
                                if len(clicks) == 0:
                                    possible_pos = last_clicked['piece']['piece'].check_position(board, current_player, p1)
                                    board.update(screen, current_player, text_details)
                                    game.show_possible_moves(possible_pos, screen, surface, board, current_player, p1)
                                    clicks.append({'piece': last_clicked, 'possible_pos': possible_pos})
                                    break

                                # Select a different/same piece
                                else:
                                    possible_pos = last_clicked['piece']['piece'].check_position(board, current_player, p1)
                                    board.update(screen, current_player, text_details)
                                    game.show_possible_moves(possible_pos, screen, surface, board, current_player, p1)
                                    clicks.pop()
                                    clicks.append({'piece': last_clicked, 'possible_pos': possible_pos})
                                    break
                            
                            # Select enemy piece
                            else:
                                if len(clicks) > 0:
                                    last_clicked = p
                                    if last_clicked in clicks[0]['possible_pos']:
                                        clicks.append({'piece': last_clicked})
                                        break
                                    else:
                                        game.empty_list(clicks)

            # Move piece
            if len(clicks) == 2:
                board.move_piece(current_player, clicks[0]['piece'], clicks[1]['piece'], p1, p2)
                board.update(screen, current_player, text_details)
                game.remove_en_passant(p1, p2)

                # Check if piece can be promoted
                board.check_piece_promotion(clicks[0]['piece'], current_player, screen, text_details, 0, p1)

                # Get next player and update game
                game.empty_list(clicks)
                current_player = game.next_turn(current_player, turn_order, p1, p2)
                text_details['total_turns'] += 1
                board.update(screen, current_player, text_details)

                # Check for game over
                game_over = game.check_mate(current_player, p1, p2)

                # Check for draw (W.I.P.)
    
        if game_over and game_over_count == 0:
            game.game_over(current_player, p1, p2, text_details, screen, size, game_draw)
            game_over_count += 1

    pygame.display.update()

pygame.quit()
