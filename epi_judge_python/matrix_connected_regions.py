from test_framework import generic_test


def flip_color(x, y, image):
    # TODO - you fill in here.
    def is_valid_point(x, y, color):
        return 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == color

    def explore_color(x, y, color):
        if not is_valid_point(x, y, color):
            return

        image[x][y] = not color

        for dx, dy in [(0, -1), (0, +1), (-1, 0), (+1, 0)]:
            explore_color(x + dx, y + dy, color)

    color = image[x][y]
    explore_color(x, y, color)

    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
