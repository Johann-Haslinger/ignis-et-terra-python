from enum import Enum, auto


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
SPEED = 200
PLAYER_START_X = 800
PLAYER_START_Y = 400
RED = (255, 0, 0)
PLAYER_WIDTH = 200
PLAYER_HEIGHT = 200
TILE_SIZE = 80



LAYERS = {
    'ground': 0,
    'main': 1
}


class ANIMATION(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    UP_IDLE = "up_idle"
    DOWN_IDLE = "down_idle"
    LEFT_IDLE = "left_idle"
    RIGHT_IDLE = "right_idle"
    