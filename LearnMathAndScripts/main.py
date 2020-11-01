import pygame
import globals

from menu import Menu

pygame.init()
clock = pygame.time.Clock()

game_screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))

menu = Menu()

while True:
    clock.tick(globals.FRAME_RATE)

    menu.render(game_screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
