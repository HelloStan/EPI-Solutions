from test_framework import generic_test


def roman_to_integer(s):
    # TODO - you fill in here.
    maping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    sum = 0
    prev_d = float('inf')
    for c in s:
        d = maping[c]
        sum += d
        if d > prev_d:
            sum -= 2 * prev_d

        prev_d = d

    return sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
