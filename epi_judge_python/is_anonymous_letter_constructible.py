from test_framework import generic_test
from collections import defaultdict


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # TODO - you fill in here.
    counter = defaultdict(int)

    for c in magazine_text:
        counter[c] += 1

    for c in letter_text:
        counter[c] -= 1
        if counter[c] < 0:
            return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
