import pygame
import globals

from menu import Menu
from gradients import vertical
from person import Person
from control import Control
from monitor import Monitor
from folder import Folder

pygame.font.init()

clock = pygame.time.Clock()

game_screen = pygame.display.set_mode([globals.WIDTH, globals.HEIGHT])
itens = pygame.image.load('resources/images/itens.png')
font = pygame.font.SysFont("Arial", 18)
menu = Menu()
mained = Person(75, 2, (globals.WIDTH - 38) / 2, (globals.HEIGHT - 58) / 2, 38, 58)

lr = [[75, 11, 139], [78, 13, 141], [77, 13, 141], [76, 12, 139]]
folders = [[75, 75, 'airplane.png']]

for folder in folders:
	folder[2] = pygame.image.load(globals.IMAGE_DIR.format(folder[2])).convert_alpha()

def maske_blit(win, img, wx, wy, x, y, w, h):
	pygame.draw.rect(game_screen, (255, 0, 0), (x, y, w, h), 2)
	surf = pygame.Surface((w, h), pygame.SRCALPHA).convert_alpha()
	surf.blit(img, (0, 0), (wx, wy, w, h))
	win.blit(surf, (x, y))

def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render("FPS: {}".format(fps), 1, pygame.color.Color("blue"))
	return fps_text

monitor = Monitor(game_screen)
control = Control()
gradient = vertical((game_screen.get_width(), game_screen.get_height()), (25, 111, 247, 255), (180, 207, 250, 255))

while pygame.event.poll().type != pygame.QUIT:

	clock.tick(globals.FRAME_RATE)

	game_screen.blit(gradient, (0, 0))

	surface = monitor.draw(game_screen)
	
	control.use(mained, game_screen, surface)

	menu.render(game_screen)
	
	for folder in folders:
		Folder(folder[0], folder[1], game_screen, folder[2])

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.VIDEORESIZE:
			monitor = Monitor(game_screen)
			mained = Person(75, 2, (game_screen.get_width() - 38) / 2, (game_screen.get_height() - 58) / 2, 38, 58)
		if event.type == pygame.KEYUP:
			if (event.key == pygame.K_w) or (event.key == pygame.K_s) or (event.key == pygame.K_a) or (
					event.key == pygame.K_d):
				control.reset()

	maske_blit(game_screen,
		itens,
		lr[control.dir][int(control.mov / 10)],
		control.top,
		mained.x,
		mained.y,
		mained.w,
		mained.h)
	game_screen.blit(update_fps(),(10, 0))

	pygame.display.flip()
