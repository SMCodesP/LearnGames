import os.path as path

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FRAME_RATE = 120

AUDIO_DIR = path.join(path.dirname(path.abspath(__file__)), 'resources', 'audio', '{0}')
IMAGE_DIR = path.join(path.dirname(path.abspath(__file__)), 'resources', 'images', '{0}')
