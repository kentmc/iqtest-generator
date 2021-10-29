import math
import random
from typing import List

from changing_attribute import ChangingAttribute
from config import Config
from object import Object


class Map:
    grid: List[List[List[Object]]]
    objects: List[Object]

    def __init__(self, level: int):

        self.grid = [
            [[], [], []],
            [[], [], []],
            [[], [], []]
        ]
        self.objects = []

        num_objects = 1 + math.floor(level / (len(ChangingAttribute) + 1))
        for i in range(0, num_objects):
            x, y = self.find_new_object_position()
            self.add_object(x, y)

        changing_attributes_remaining = level
        while True:
            nothing_changed = True
            for obj in self.objects:
                if changing_attributes_remaining <= 0:
                    break
                if obj.add_random_changing_attribute():
                    changing_attributes_remaining -= 1
                    nothing_changed = False
            if nothing_changed:
                break

    def find_new_object_position(self):
        x = random.randint(0, Config.num_cells - 1)
        y = random.randint(0, Config.num_cells - 1)
        #  keep retrying if there is an empty position and we didn't find one randomly
        if self.empty_position_exists():
            while True:
                if self.position_is_empty(x, y):
                    break
                x = random.randint(0, Config.num_cells - 1)
                y = random.randint(0, Config.num_cells - 1)
        return x, y

    def add_object(self, x, y):
        obj = Object(x, y)
        self.grid[obj.x][obj.y].append(obj)
        self.objects.append(obj)

    def iterate(self):
        self.clear_grid()
        for obj in self.objects:
            obj.iterate()

        # put all objects back in grid
        for obj in self.objects:
            self.grid[obj.x][obj.y].append(obj)

    def empty_position_exists(self):
        for row in self.grid:
            for cell in row:
                if len(cell) == 0:
                    return True
        return False

    def position_is_empty(self, x, y):
        return len(self.grid[x][y]) == 0

    def clear_grid(self):
        for row in self.grid:
            for cell in row:
                cell.clear()

    def clone(self):
        map = Map(0)
        map.clear_grid()
        map.objects = []
        for obj in self.objects:
            cloned_obj = obj.clone()
            map.objects.append(cloned_obj)
            map.grid[obj.x][obj.y].append(cloned_obj)
        return map

    def mutate(self):
        self.clear_grid()

        random_obj = self.objects[random.randint(0, len(self.objects) - 1)]
        random_obj.mutate()

        # put all objects back in grid
        for obj in self.objects:
            self.grid[obj.x][obj.y].append(obj)
        return self
