import random

from artist import Artist
from map import Map


class Puzzle:

    sequence_images = []
    solution_choices = []

    def __init__(self, difficulty, num_images, num_solution_choices):
        self.sequence_images = []
        self.solution_choices = []

        map = Map(difficulty)

        # Generate logical sequence
        self.sequence_images.append(Artist.draw_map(map))
        for i in range(0, num_images - 1):
            map.iterate()
            self.sequence_images.append(Artist.draw_map(map))
        # Generate solution choices
        # - Add correct solution
        map.iterate()
        correct_solution = map.clone()
        self.solution_choices.append(correct_solution)
        # - Add random mutations as solution choices
        while len(self.solution_choices) < num_solution_choices:
            wrong_solution = correct_solution.clone().mutate()
            if not any(Artist.is_identical(solution_choice, wrong_solution) for solution_choice in self.solution_choices):
                self.solution_choices.append(wrong_solution)
        random.shuffle(self.solution_choices)


    def draw(self):
        solution_choice_images = [Artist.draw_map(solution_choice) for solution_choice in self.solution_choices]
        empty_picture = Artist.draw_empty_grid()
        return Artist.create_plot(self.sequence_images, solution_choice_images, empty_picture)
