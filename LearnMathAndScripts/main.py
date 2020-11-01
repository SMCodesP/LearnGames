import pygame
import globals

from menu import Menu
from person import Person
from control import Control
from monitor import Monitor

pygame.init()
clock = pygame.time.Clock()

pixels = []
flags = pygame.RESIZABLE
game_screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT), flags)
itens = pygame.image.load('resources/images/itens.png')
font = pygame.font.SysFont("Arial", 18)
menu = Menu()
mained = Person(75, 2, (globals.WIDTH - 38) / 2, (globals.HEIGHT - 58) / 2, 38, 58)

lr = [[75, 11, 139], [78, 13, 141], [77, 13, 141], [76, 12, 139]]

def maske_blit(win, img, wx, wy, x, y, w, h):
    pygame.draw.rect(game_screen, (255, 0, 0), (x, y, w, h), 2)
    surf = pygame.Surface((w, h), pygame.SRCALPHA).convert_alpha()
    surf.blit(img, (0, 0), (wx, wy, w, h))
    win.blit(surf, (x, y))

def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render("FPS: {}".format(fps), 1, pygame.color.Color("blue"))
    return fps_text


control = Control()
monitor = Monitor(game_screen)

running = True
while running:
    for i in range(game_screen.get_width()):
        for j in range(game_screen.get_height()):
            pixels.append(game_screen.get_at((i, j)))

    control.use(mained, pixels)

    clock.tick(globals.FRAME_RATE)

    menu.render(game_screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.VIDEORESIZE:
            monitor = Monitor(game_screen)
            mained = Person(75, 2, (game_screen.get_width() - 38) / 2, (game_screen.get_height() - 58) / 2, 38, 58)
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_w) or (event.key == pygame.K_s) or (event.key == pygame.K_a) or (
                    event.key == pygame.K_d):
                control.reset()

    game_screen.fill((66, 135, 245))

    monitor.draw(game_screen)

    maske_blit(game_screen, itens, lr[control.dir][int(control.mov / 10)], control.top, mained.x, mained.y, mained.w,
               mained.h)
    game_screen.blit(update_fps(), (10, 0))

    pygame.display.flip()
