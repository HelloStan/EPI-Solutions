from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    # TODO - you fill in here.
    negative = False
    if x < 0:
        negative = True
        x = -x

    s = []
    while True:
        d = x % 10
        x //= 10

        s.append(chr(d + 0x30))

        if x == 0:
            break

    if negative:
        s.append("-")

    s = "".join(reversed(s))

    return s


def string_to_int(s):
    # TODO - you fill in here.
    negative = s[0] == '-'
    if s[0] == '-':
        s = s[1:]

    x = 0
    for c in s:
        x = x * 10 + ord(c) - 0x30

    if negative:
        x = -x

    return x


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
