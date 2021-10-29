import random


class MovePattern:
    dx = 0
    dy = 0

    @staticmethod
    def random():
        move_pattern = MovePattern()
        while move_pattern.dx == 0 and move_pattern.dy == 0:
            move_pattern.dx = random.randint(0, 4) - 2
            move_pattern.dy = random.randint(0, 4) - 2
        return move_pattern




