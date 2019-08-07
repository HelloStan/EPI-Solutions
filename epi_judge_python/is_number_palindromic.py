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


def is_palindrome_number(x):
    # TODO - you fill in here.
    rev_x = reverse(x)

    return x >= 0 and x == rev_x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
