import pygame

class Folder:
    def __init__(self, x, y, screen, image):
        myfont = pygame.font.SysFont('Comic Sans MS', 17)
        textsurface = myfont.render('Jogo do avião', False, (0, 0, 0))
        image = pygame.transform.scale(image, (50, 50))
        screen.blit(image, (x, y))
        screen.blit(textsurface, (x-10,y+50))
