import pygame


class Control:
    def __init__(self):
        self.dir = 0
        self.mov = 0
        self.top = 2

    def use(self, obj, pixels):
        key = pygame.key.get_pressed()

        if key[pygame.K_s]:
            self.mov += 1
            self.dir = 0
            self.top = 2
            obj.y += 1
            for pixel in pixels:
                if (pixel == (54, 50, 51)):
                    print(pixel)

        if key[pygame.K_w]:
            self.mov += 1
            self.dir = 3
            self.top = 193
            obj.y -= 1

        if key[pygame.K_a]:
            self.mov += 1
            self.dir = 1
            self.top = 65
            obj.x -= 1

        if key[pygame.K_d]:
            self.mov += 1
            self.dir = 2
            self.top = 129
            obj.x += 1

        if self.mov > 29:
            self.mov = 0
        elif self.mov < 0:
            self.mov = 29

    def reset(self):
        self.mov = 0
        self.dir = 0
        self.top = 2
