from test_framework import generic_test
import math


def square_root(x):
    # TODO - you fill in here.
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)

    while not math.isclose(left, right):
        m = (left + right) / 2

        if m ** 2 > x:
            right = m
        else:
            left = m

    print(x, left)
    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("real_square_root.py",
                                       'real_square_root.tsv', square_root))
