import random
from typing import List

from color import Color


class ColorPattern:

    color_sequence: List[Color] = []

    @staticmethod
    def random(start_color: Color, num_colors):
        color_pattern = ColorPattern()
        color_pattern.color_sequence = [start_color]
        random_colors: List[Color] = list(Color)
        random.shuffle(random_colors)
        while len(random_colors) > 0 and len(color_pattern.color_sequence) < num_colors:
            color = random_colors.pop()
            if color != start_color:
                color_pattern.color_sequence.append(color)
        return color_pattern







