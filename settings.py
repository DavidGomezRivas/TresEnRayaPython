import pygame

def initialize_screen():
    pygame.init()
    infoObject = pygame.display.Info()
    width, height = int(infoObject.current_w * 0.8), int(infoObject.current_h * 0.8)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tres en Raya")
    return screen, width, height

gray = (128, 128, 128)
