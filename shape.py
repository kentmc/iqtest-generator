import random
from enum import Enum


class Shape(Enum):
    SQUARE = 1
    CIRCLE = 2
    HORIZONTAL_LINE = 3
    VERTICAL_LINE = 4

    @staticmethod
    def random():
        return Shape(random.randint(1, 4))
