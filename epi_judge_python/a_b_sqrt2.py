from test_framework import generic_test
from sortedcontainers import SortedDict


def generate_first_k_a_b_sqrt2(k):
    # TODO - you fill in here.
    candidates = SortedDict()

    candidates[0] = (0, 0)

    result = []
    while candidates and len(result) < k:
        v, (a, b) = candidates.popitem(0)

        result.append(v)

        candidates[(a + 1) + b * 2 ** 0.5] = a + 1, b
        candidates[a + (b + 1) * 2 ** 0.5] = a, b + 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("a_b_sqrt2.py", 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
