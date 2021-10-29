import random
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    WHITE = 4
    BLACK = 5
    YELLOW = 6
    CYAN = 7
    MAGENTA = 8

    @staticmethod
    def random():
        return Color(random.randint(1, 5))

    def get_red_channel(self):
        if self == Color.RED:
            return 255
        elif self == Color.GREEN:
            return 0
        elif self == Color.BLUE:
            return 0
        elif self == Color.WHITE:
            return 255
        elif self == Color.BLACK:
            return 0
        elif self == Color.YELLOW:
            return 255
        elif self == Color.CYAN:
            return 0
        elif self == Color.MAGENTA:
            return 255
        else:
            return 0

    def get_green_channel(self):
        if self == Color.RED:
            return 0
        elif self == Color.GREEN:
            return 255
        elif self == Color.BLUE:
            return 0
        elif self == Color.WHITE:
            return 255
        elif self == Color.BLACK:
            return 0
        elif self == Color.YELLOW:
            return 255
        elif self == Color.CYAN:
            return 255
        elif self == Color.MAGENTA:
            return 0
        else:
            return 0

    def get_blue_channel(self):
        if self == Color.RED:
            return 0
        elif self == Color.GREEN:
            return 0
        elif self == Color.BLUE:
            return 255
        elif self == Color.WHITE:
            return 0
        elif self == Color.BLACK:
            return 0
        elif self == Color.YELLOW:
            return 0
        elif self == Color.CYAN:
            return 255
        elif self == Color.MAGENTA:
            return 255
        else:
            return 0
