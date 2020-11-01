class Person:
    def __init__(self, wx, wy, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.wx = wx
        self.wy = wy
        self.hitbox = (self.x, self.y, self.w, self.h)
