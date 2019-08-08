import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A):
    # TODO - you fill in here.
    minumum = A[0]
    maximum = A[0]

    for i in range(0, len(A) - 1, 2):
        if A[i] < A[i + 1]:
            loc_min = A[i]
            loc_max = A[i + 1]
        else:
            loc_min = A[i + 1]
            loc_max = A[i]

        if loc_max > maximum:
            maximum = loc_max
        if loc_min < minumum:
            minumum = loc_min

    if len(A) % 2:
        minumum = min(minumum, A[-1])
        maximum = max(maximum, A[-1])

    return MinMax(minumum, maximum)


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_min_max_in_array.py",
            'search_for_min_max_in_array.tsv',
            find_min_max,
            res_printer=res_printer))
