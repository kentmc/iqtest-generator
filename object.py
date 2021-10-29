import random
from typing import List

from changing_attribute import ChangingAttribute
from color import Color
from color_pattern import ColorPattern
from config import Config
from move_pattern import MovePattern
from shape import Shape
from shape_pattern import ShapePattern


class Object:
    x: int
    y: int
    shape: Shape
    color: Color
    bounces_at_wall: bool
    move_pattern: MovePattern
    color_pattern: ColorPattern
    shape_pattern: ShapePattern

    changing_attributes_applied: List[ChangingAttribute]
    changing_attribute_choices: List[ChangingAttribute]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = Shape.random()
        self.color = Color.random()
        self.bounces_at_wall = random.randint(0, 1) == 1
        self.move_pattern = None
        self.color_pattern = None
        self.shape_pattern = None

        self.changing_attribute_choices = list(ChangingAttribute)
        self.changing_attributes_applied = []
        random.shuffle(self.changing_attribute_choices)

    def add_random_changing_attribute(self):
        if len(self.changing_attribute_choices) == 0:
            return False
        self.add_changing_attribute(self.changing_attribute_choices.pop())
        return True

    def add_changing_attribute(self, attribute):
        if attribute == ChangingAttribute.POSITION:
            self.move_pattern = MovePattern.random()
        if attribute == ChangingAttribute.COLOR:
            self.color_pattern = ColorPattern.random(self.color, 3)
        if attribute == ChangingAttribute.SHAPE:
            self.shape_pattern = ShapePattern.random(self.shape, 3)
        self.changing_attributes_applied.append(attribute)

    def iterate(self):
        self.handle_move()
        self.handle_shape()
        self.handle_color()

    def handle_move(self):
        if self.move_pattern is None:
            return
        self.x += self.move_pattern.dx
        self.y += self.move_pattern.dy
        if self.bounces_at_wall:
            if self.x < 0:
                self.x = -self.x
                self.move_pattern.dx = -self.move_pattern.dx
            if self.x >= Config.num_cells:
                self.x = 2 * Config.num_cells - self.x - 2
                self.move_pattern.dx = -self.move_pattern.dx
            if self.y < 0:
                self.y = -self.y
                self.move_pattern.dy = -self.move_pattern.dy
            if self.y >= Config.num_cells:
                self.y = 2 * Config.num_cells - self.y - 2
                self.move_pattern.dy = -self.move_pattern.dy
        else:  # warp
            self.x = self.x % Config.num_cells
            self.y = self.y % Config.num_cells

    def handle_shape(self):
        if self.shape_pattern is None:
            return
        index = self.shape_pattern.shape_sequence.index(self.shape)
        new_index = (index + 1) % len(self.shape_pattern.shape_sequence)
        self.shape = self.shape_pattern.shape_sequence[new_index]

    def handle_color(self):
        if self.color_pattern is None:
            return
        try:
            index = self.color_pattern.color_sequence.index(self.color)
            new_index = (index + 1) % len(self.color_pattern.color_sequence)
            self.color = self.color_pattern.color_sequence[new_index]
        except Exception:
            a = 2

    def clone(self):
        cloned_obj = Object(self.x, self.y)
        cloned_obj.shape = self.shape
        cloned_obj.color = self.color
        cloned_obj.bounces_at_wall = self.bounces_at_wall

        if self.move_pattern is not None:
            cloned_obj.move_pattern = MovePattern()
            cloned_obj.move_pattern.dx = self.move_pattern.dx
            cloned_obj.move_pattern.dy = self.move_pattern.dy

        if self.color_pattern is not None:
            cloned_obj.color_pattern = ColorPattern()
            cloned_obj.color_pattern.color_sequence = []
            for color in self.color_pattern.color_sequence:
                cloned_obj.color_pattern.color_sequence.append(color)

        if self.shape_pattern is not None:
            cloned_obj.shape_pattern = ShapePattern()
            cloned_obj.shape_pattern.shape_sequence = []
            for shape in self.shape_pattern.shape_sequence:
                cloned_obj.shape_pattern.shape_sequence.append(shape)

        cloned_obj.changing_attribute_choices = [a for a in self.changing_attribute_choices]
        cloned_obj.changing_attributes_applied = [a for a in self.changing_attributes_applied]
        return cloned_obj

    def mutate(self):
        attribute_to_change = None
        #  prefer to change an attribute the object already has on it's list of changing attributes
        if len(self.changing_attributes_applied) > 0 and random.randint(1, 100) > 80:
            random_attribute_index = random.randint(0, len(self.changing_attributes_applied) - 1)
            attribute_to_change = self.changing_attributes_applied[random_attribute_index]
        if attribute_to_change is None:
            random_attributes = list(ChangingAttribute)
            random.shuffle(random_attributes)
            attribute_to_change = random_attributes[0]

        if attribute_to_change == ChangingAttribute.POSITION:  # move
            self.mutate_position()
        elif attribute_to_change == ChangingAttribute.SHAPE:  # change shape
            self.mutate_shape()
        elif attribute_to_change == ChangingAttribute.COLOR:  # change color
            self.mutate_color()

    def mutate_color(self):
        #  prefer existing color sequence if it exists
        if self.color_pattern is None or random.randint(1, 100) > 80:
            color_list = [color for color in list(Color) if color != self.color]
        else:
            color_list = [color for color in self.color_pattern.color_sequence if color != self.color]
        random.shuffle(color_list)
        self.color = color_list[0]

    def mutate_shape(self):
        #  prefer existing shape sequence if it exists
        if self.shape_pattern is None or random.randint(1, 100) > 80:
            shape_list = [shape for shape in list(Shape) if shape != self.shape]
        else:
            shape_list = [shape for shape in self.shape_pattern.shape_sequence if shape != self.shape]
        random.shuffle(shape_list)
        self.shape = shape_list[0]

    def mutate_position(self):
        deltaXs = []
        deltaYs = []
        if self.x > 0:
            deltaXs.append(-1)
        if self.x < Config.num_cells - 1:
            deltaXs.append(1)
        if self.y > 0:
            deltaYs.append(-1)
        if self.y < Config.num_cells - 1:
            deltaYs.append(1)
        random.shuffle(deltaXs)
        random.shuffle(deltaYs)
        r = random.randint(1, 100)
        if r > 80:  # prefer to only change position in 1 plane
            if random.randint(0, 1) == 1:  # move x
                self.x += deltaXs[0]
            else:  # move y
                self.y += deltaYs[0]
        else:
            self.x += deltaXs[0]
            self.y += deltaYs[0]
