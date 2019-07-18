from test_framework import generic_test
from test_framework.test_failure import TestFailure
from itertools import tee


def find_missing_element(stream):
    # TODO - you fill in here.
    prefix = 0

    for shift in [24, 16, 8, 0]:
        count = {i: 0 for i in range(256)}
        prefix_mask = 0xFFFFFF00 << shift
        stream, stream_copy = tee(stream)

        for e in stream_copy:
            if e & prefix_mask == prefix:
                byte = (e >> shift) & 0xFF
                count[byte] += 1

        max_count = 2 ** shift
        for key in sorted(count.keys()):
            if count[key] < max_count:
                prefix += key << shift
                break

    return prefix


def find_missing_element_wrapper(data):
    try:
        return find_missing_element(iter(data))
    except ValueError:
        raise TestFailure('Unexpected no_missing_element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("absent_value_array.py",
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
