import pygame
import globals

from menu import Menu
from person import Person
from control import Control

pygame.init()
clock = pygame.time.Clock()

game_screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
itens = pygame.image.load('resources/images/itens.png')
font = pygame.font.SysFont("Arial", 18)
menu = Menu()
mained = Person(75, 2, 200, 490, 38, 58)

lr = [[75, 11, 139], [78, 13, 141], [77, 13, 141], [76, 12, 139]]


def maske_blit(win, img, wx, wy, x, y, w, h):
    surf = pygame.Surface((w, h), pygame.SRCALPHA).convert_alpha()
    surf.blit(img, (0, 0), (wx, wy, w, h))
    win.blit(surf, (x, y))

def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render("FPS: {}".format(fps), 1, pygame.color.Color("blue"))
    return fps_text

control = Control()

while True:

    control.use(mained)

    clock.tick(globals.FRAME_RATE)

    menu.render(game_screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_w) or (event.key == pygame.K_s) or (event.key == pygame.K_a) or (event.key == pygame.K_d):
                control.reset()

    game_screen.fill(globals.WHITE)

    maske_blit(game_screen, itens, lr[control.dir][int(control.mov / 10)], control.top, mained.x, mained.y, mained.w, mained.h)
    game_screen.blit(update_fps(), (10, 0))

    pygame.display.flip()

