from test_framework import generic_test


def square_root(k):
    # TODO - you fill in here.
    a = 0
    b = k

    while a <= b:
        x = (a + b) // 2
        x_squared = x ** 2

        if k >= x_squared:
            a = x + 1
        else:
            b = x - 1

    return a - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
