import random
from typing import List

from shape import Shape
from shape import Shape


class ShapePattern:

    shape_sequence: List[Shape] = []

    @staticmethod
    def random(start_shape: Shape, num_shapes):
        shape_pattern = ShapePattern()
        shape_pattern.shape_sequence = [start_shape]
        random_shapes: List[Shape] = list(Shape)
        random.shuffle(random_shapes)
        while len(random_shapes) > 0 and len(shape_pattern.shape_sequence) < num_shapes:
            shape = random_shapes.pop()
            if shape != start_shape:
                shape_pattern.shape_sequence.append(shape)
        return shape_pattern







