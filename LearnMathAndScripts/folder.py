import pygame
import globals

class Folder:
	def __init__(self, x, y, screen, image):
		myfont = pygame.font.SysFont('Comic Sans MS', 17)
		textsurface = myfont.render('Jogo do avião', False, (0, 0, 0))

		self.surface = pygame.Surface((textsurface.get_width()+10, 64), pygame.SRCALPHA)

		image_render = pygame.transform.scale(image, (48, 48))
		self.surface.blit(image_render, ((self.surface.get_width()-image_render.get_width())/2, 0))

		self.surface.blit(textsurface, ((self.surface.get_width()-textsurface.get_width())/2, (self.surface.get_height()-textsurface.get_height())))

		pygame.draw.rect(self.surface, (255, 0, 0), (0, 0, self.surface.get_width(), self.surface.get_height()), 2)

		screen.blit(self.surface, (x, y))
