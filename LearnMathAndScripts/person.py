class Person:
    def __init__(self, wx, wy, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.wx = wx
        self.wy = wy

        self.default_x = x
        self.default_y = y
        self.default_w = w
        self.default_h = h
        self.default_wx = wx
        self.default_wy = wy

    def reset(self):
        self.x = self.default_x
        self.y = self.default_y
        self.w = self.default_w
        self.h = self.default_h
        self.wx = self.default_wx
        self.wy = self.default_wy