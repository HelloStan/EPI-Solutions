import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from collections import defaultdict

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph, keywords):
    # TODO - you fill in here.
    counter = defaultdict(int)
    to_cover = len(keywords)
    left = 0
    result = None
    for right, word in enumerate(paragraph):
        if word in keywords:
            if counter[word] == 0:
                to_cover -= 1
            counter[word] += 1

        while to_cover == 0:
            if result is None or (right - left < result[1] - result[0]):
                result = Subarray(left, right)

            word_left = paragraph[left]
            if word_left in keywords:
                counter[word_left] -= 1
                if counter[word_left] == 0:
                    to_cover += 1
            left += 1

    return result


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))
