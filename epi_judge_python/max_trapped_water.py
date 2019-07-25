from test_framework import generic_test


def get_max_trapped_water(heights):
    # TODO - you fill in here.
    i = 0
    j = len(heights) - 1

    max_area = 0
    while i < j:
        area = min(heights[i], heights[j]) * (j - i)
        max_area = max(max_area, area)

        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1

    return max_area


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_trapped_water.py",
                                       "max_trapped_water.tsv",
                                       get_max_trapped_water))
