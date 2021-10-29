from puzzle import Puzzle

difficulty = 7
num_images = 5
num_solution_choices = 12

puzzle = Puzzle(difficulty, num_images, num_solution_choices)
plot = puzzle.draw()
plot.show()
# You can save the plot using plot.savefig("test/a.png")

