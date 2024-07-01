import pygame

def handle_events(board, current_player, width, height):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, current_player

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // (height // 3), x // (width // 3)
            if board[row][col] == "":
                board[row][col] = current_player
                current_player = "O" if current_player == "X" else "X"
    return True, current_player
