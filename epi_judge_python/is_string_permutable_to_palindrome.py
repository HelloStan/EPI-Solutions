from test_framework import generic_test
from collections import defaultdict


def can_form_palindrome(s):
    # TODO - you fill in here.
    counts = defaultdict(int)

    for c in s:
        counts[c] += 1

    num_odd = 0
    for v in counts.values():
        if v % 2:
            num_odd += 1

    return num_odd <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
