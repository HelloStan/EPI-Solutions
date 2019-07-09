from test_framework import generic_test


def power(x, y):
    # TODO - you fill in here.
    if y < 0:
        x = 1.0 / x
        y = -y

    result = 1
    while y:
        if y & 1:
            result *= x

        y >>= 1
        x **= 2

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
