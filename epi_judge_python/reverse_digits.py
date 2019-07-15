from test_framework import generic_test


def reverse(x):
    # TODO - you fill in here.
    x_rev = 0
    negative = False
    if x < 0:
        x = -x
        negative = True

    while x:
        d = x % 10
        x_rev = 10 * x_rev + d

        x //= 10

    if negative:
        x_rev = -x_rev

    return x_rev


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
