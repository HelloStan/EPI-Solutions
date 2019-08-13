from test_framework import generic_test


def calculate_largest_rectangle(heights):
    # TODO - you fill in here.
    pillars = []
    max_area = 0

    for i, h in enumerate(heights + [0]):
        while pillars and heights[pillars[-1]] >= h:
            height = heights[pillars.pop()]
            width = i - pillars[-1] - 1 if pillars else i
            area = width * height
            max_area = max(max_area, area)

        pillars.append(i)

    return max_area


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("largest_rectangle_under_skyline.py",
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
