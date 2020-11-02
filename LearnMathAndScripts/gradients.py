import pygame

def vertical(size, start_color, end_color):
    height = size[1]
    bigSurf = pygame.Surface((1, height)).convert_alpha()
    dd = 1.0/height
    sr, sg, sb, sa = start_color
    er, eg, eb, ea = end_color

    rm = (er-sr)*dd
    gm = (eg-sg)*dd
    bm = (eb-sb)*dd
    am = (ea-sa)*dd

    for y in range(height):
        bigSurf.set_at((0, y), (int(sr + rm*y), int(sg + gm*y), int(sb + bm*y), int(sa + am*y)))

    return pygame.transform.scale(bigSurf, size)