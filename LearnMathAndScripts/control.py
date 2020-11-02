import pygame


class Control:
    def __init__(self):
        self.dir = 0
        self.mov = 0
        self.top = 2

    def use(self, obj, screen, monitor_surface):
        key = pygame.key.get_pressed()

        if key[pygame.K_s]:
            self.mov += 1
            self.dir = 0
            self.top = 2
            if monitor_surface.get_at((int(obj.x), int(obj.y+1)+obj.h)) != (119, 147, 147, 255):
                obj.y += 1

        if key[pygame.K_w]:
            self.mov += 1
            self.dir = 3
            self.top = 193
            if monitor_surface.get_at((int(obj.x), int(obj.y-1))) != (119, 147, 147, 255):
                obj.y -= 1

        if key[pygame.K_a]:
            self.mov += 1
            self.dir = 1
            self.top = 65
            if monitor_surface.get_at((int(obj.x-1), int(obj.y)+obj.h)) != (119, 147, 147, 255):
                obj.x -= 1

        if key[pygame.K_d]:
            self.mov += 1
            self.dir = 2
            self.top = 129
            if monitor_surface.get_at((int(obj.x+1)+obj.w, int(obj.y)+obj.h)) != (119, 147, 147, 255):
                obj.x += 1

        if self.mov > 29:
            self.mov = 0
        elif self.mov < 0:
            self.mov = 29

    def reset(self):
        self.mov = 0
        self.dir = 0
        self.top = 2
