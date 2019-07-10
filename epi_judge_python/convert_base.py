from test_framework import generic_test


def convert_base(num_as_string, b1, b2):
    # TODO - you fill in here.
    map_c2d = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }
    map_d2c = "0123456789ABCDEF"

    negative = False
    if num_as_string[0] == '-':
        negative = True
        num_as_string = num_as_string[1:]

    num = 0
    for c in num_as_string:
        num = num * b1 + map_c2d[c]

    converted_string = []
    while num:
        converted_string.append(map_d2c[num % b2])
        num //= b2

    if len(converted_string) == 0:
        converted_string.append('0')

    if negative:
        converted_string.append("-")

    converted_string = "".join(reversed(converted_string))

    return converted_string


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
