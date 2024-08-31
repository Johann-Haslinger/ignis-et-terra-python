from enum import Enum, auto


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

SPEED = 200

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
    