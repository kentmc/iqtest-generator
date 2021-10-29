from math import ceil
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

from config import Config
from map import Map
from object import Object
from shape import Shape


class Artist:

    @staticmethod
    def draw_map(map: Map):
        image = Artist.draw_empty_grid()
        image_draw: ImageDraw = ImageDraw.Draw(image)
        Artist.__draw_objects(image_draw, map)
        return image

    @staticmethod
    def __draw_objects(image_draw: ImageDraw, map: Map):
        for obj in map.objects:
            x_pos = Config.cell_size / 2 + Config.cell_size * obj.x
            y_pos = Config.cell_size / 2 + Config.cell_size * obj.y
            Artist.__draw_object(image_draw, obj, x_pos, y_pos)

    @staticmethod
    def __draw_object(image_draw: ImageDraw, obj: Object, x: int, y: int):
        red = obj.color.get_red_channel()
        green = obj.color.get_green_channel()
        blue = obj.color.get_blue_channel()
        alpha = 0

        if obj.shape == Shape.CIRCLE:
            r = Config.cell_size/2 - 2
            image_draw.ellipse((x - r, y - r, x + r, y + r), fill=(red, green, blue, alpha))
        if obj.shape == Shape.SQUARE:
            size = Config.cell_size - 2
            image_draw.rectangle([x - size / 2, y - size / 2, x + size / 2, y + size / 2], fill=(red, green, blue, alpha))
        if obj.shape == Shape.HORIZONTAL_LINE:
            size_hor = Config.cell_size - 2
            size_ver = Config.cell_size / 2 - 2
            image_draw.rectangle([x - size_hor / 2, y - size_ver / 2, x + size_hor / 2, y + size_ver / 2],
                                 fill=(red, green, blue, alpha))
        if obj.shape == Shape.VERTICAL_LINE:
            size_hor = Config.cell_size / 2 - 2
            size_ver = Config.cell_size - 2
            image_draw.rectangle([x - size_hor / 2, y - size_ver / 2, x + size_hor / 2, y + size_ver / 2],
                                 fill=(red, green, blue, alpha))

    @staticmethod
    def draw_empty_grid():
        width = Config.num_cells * Config.cell_size
        height = Config.num_cells * Config.cell_size
        image = Image.new(mode="RGB", size=(width, height), color=(100, 100, 100, 0))
        return image

    @staticmethod
    def is_identical(map1, map2):
        im1 = Artist.draw_map(map1)
        im2 = Artist.draw_map(map2)
        return list(im1.getdata()) == list(im2.getdata())

    @staticmethod
    def create_plot(sequence_images, solution_choices, empty_picture):
        fig = plt.figure(figsize=(10, 10))
        cols = len(sequence_images) + 1

        # 1 row for sequence and question mark
        # 1 row for spacing
        rows = 2
        # extra rows for solution choices
        rows += ceil(len(solution_choices) / cols)

        for i in range(0, len(sequence_images)):
            fig.add_subplot(rows, cols, i+1)
            plt.imshow(sequence_images[i])
            plt.axis('off')
            plt.title('')

        fig.add_subplot(rows, cols, len(sequence_images)+1)
        plt.imshow(empty_picture)
        plt.axis('off')
        plt.title('?', fontsize=50)

        # start at cell after sequence + row of spacing
        index = cols * 2 + 1
        for i in range(0, len(solution_choices)):
            fig.add_subplot(rows, cols, index + i)
            plt.imshow(solution_choices[i])
            plt.axis('off')
            plt.title(i+1)
        return plt







