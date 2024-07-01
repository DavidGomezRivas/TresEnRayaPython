import pygame

def draw_board(screen, board, width, height):
    white = (255, 255, 255)
    black = (0, 0, 0)

    cell_width = width // 3
    cell_height = height // 3

    for row in range(1, 3):
        pygame.draw.line(screen, white, (0, row * cell_height), (width, row * cell_height), 5)
    for col in range(1, 3):
        pygame.draw.line(screen, white, (col * cell_width, 0), (col * cell_width, height), 5)

    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                draw_x(screen, col * cell_width, row * cell_height, cell_width, cell_height)
            elif board[row][col] == "O":
                draw_o(screen, col * cell_width, row * cell_height, cell_width, cell_height)

def draw_x(screen, x, y, width, height):
    red = (255, 0, 0)
    pygame.draw.line(screen, red, (x, y), (x + width, y + height), 5)
    pygame.draw.line(screen, red, (x + width, y), (x, y + height), 5)

def draw_o(screen, x, y, width, height):
    blue = (0, 0, 255)
    pygame.draw.ellipse(screen, blue, (x, y, width, height), 5)
