import pygame
import sys
from settings import initialize_screen, gray
from draw import draw_board
from events import handle_events

pygame.init()

# Configuración de la pantalla
screen, width, height = initialize_screen()

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def main_menu():
    while True:
        screen.fill(black)
        font = pygame.font.Font(None, 74)
        draw_text('Tres en Raya', font, white, screen, width // 2, height // 4)

        button_play = pygame.Rect(width // 3, height // 2, width // 3, 50)
        button_play_ai = pygame.Rect(width // 3, height // 2 + 60, width // 3, 50)
        button_how_to_play = pygame.Rect(width // 3, height // 2 + 120, width // 3, 50)
        button_quit = pygame.Rect(width // 3, height // 2 + 180, width // 3, 50)

        pygame.draw.rect(screen, blue, button_play)
        pygame.draw.rect(screen, blue, button_play_ai)
        pygame.draw.rect(screen, blue, button_how_to_play)
        pygame.draw.rect(screen, blue, button_quit)

        font = pygame.font.Font(None, 50)
        draw_text('Jugar', font, white, screen, button_play.centerx, button_play.centery)
        draw_text('Jugar contra IA', font, white, screen, button_play_ai.centerx, button_play_ai.centery)
        draw_text('Cómo jugar', font, white, screen, button_how_to_play.centerx, button_how_to_play.centery)
        draw_text('Salir', font, white, screen, button_quit.centerx, button_quit.centery)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.collidepoint(event.pos):
                    game_loop(False)
                if button_play_ai.collidepoint(event.pos):
                    game_loop(True)
                if button_how_to_play.collidepoint(event.pos):
                    how_to_play()
                if button_quit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

def how_to_play():
    running = True
    while running:
        screen.fill(black)
        font = pygame.font.Font(None, 50)
        draw_text('Cómo Jugar', font, white, screen, width // 2, height // 4)
        font = pygame.font.Font(None, 36)
        instructions = [
            "1. El juego se juega en una cuadrícula de 3x3.",
            "2. Dos jugadores se turnan para marcar las casillas.",
            "3. El primer jugador en alinear tres de sus marcas",
            "   en una fila, columna o diagonal, gana.",
            "4. Si todas las casillas están llenas y nadie ha",
            "   ganado, el juego termina en empate."
        ]
        for i, line in enumerate(instructions):
            draw_text(line, font, white, screen, width // 2, height // 3 + i * 30)

        button_back = pygame.Rect(width // 3, height // 2 + 120, width // 3, 50)
        pygame.draw.rect(screen, blue, button_back)
        draw_text('Volver', font, white, screen, button_back.centerx, button_back.centery)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.collidepoint(event.pos):
                    running = False

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]

    return None

def show_winner_message(winner):
    running = True
    while running:
        screen.fill(black)
        font = pygame.font.Font(None, 74)
        if winner:
            draw_text(f"¡Jugador {winner} gana!", font, white, screen, width // 2, height // 2)
        else:
            draw_text("¡Es un empate!", font, white, screen, width // 2, height // 2)

        button_back = pygame.Rect(width // 3, height // 2 + 120, width // 3, 50)
        pygame.draw.rect(screen, blue, button_back)
        font = pygame.font.Font(None, 50)
        draw_text('Volver al menú', font, white, screen, button_back.centerx, button_back.centery)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.collidepoint(event.pos):
                    running = False

def ai_move(board):
    # Simple AI that picks the first available spot
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                return row, col
    return None, None

def game_loop(ai_enabled):
    running = True
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    winner = None

    while running:
        if ai_enabled and current_player == "O":
            row, col = ai_move(board)
            if row is not None and col is not None:
                board[row][col] = "O"
                current_player = "X"
        else:
            running, current_player = handle_events(board, current_player, width, height)
        
        winner = check_winner(board)
        if winner or not any("" in row for row in board):
            running = False

        # Fill the background with gray
        screen.fill(gray)

        # Draw the game board
        draw_board(screen, board, width, height)

        # Update the display
        pygame.display.update()

    show_winner_message(winner)

if __name__ == "__main__":
    main_menu()
