import pygame


class Monitor:
	def __init__(self, screen):
		self.background = pygame.image.load('resources/images/monitor.png')
		self.background = pygame.transform.scale(self.background, (screen.get_width(), screen.get_height()))
		self.surface = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
		self.surface.blit(
				self.background,
				((screen.get_width() - self.background.get_width()) / 2,
				 (screen.get_height() - (self.background.get_height() - 15)) / 2))

	def draw(self, screen):
		screen.blit(self.surface, (0, 0))
		return self.surface