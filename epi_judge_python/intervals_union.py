import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals):
    # TODO - you fill in here.
    def is_intersect(a_left, a_right, b_left, b_right):
        if (a_left.val < b_right.val) and (b_left.val < a_right.val):
            return True
        if a_left.val == b_right.val and (a_left.is_closed or b_right.is_closed):
            return True
        if b_left.val == a_right.val and (b_left.is_closed or a_right.is_closed):
            return True
        return False

    intervals.sort(key=lambda x: (x.left.val, 0 if x.left.is_closed else 1))

    result = [intervals[0]]
    for left, right in intervals:
        result_left, result_right = result[-1]
        if not is_intersect(left, right, result_left, result_right):
            result.append(Interval(left, right))
        else:
            if right.val > result_right.val or (right.val == result_right.val and right.is_closed):
                result[-1] = Interval(result_left, right)

    return result


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intervals_union.py",
                                       "intervals_union.tsv",
                                       union_of_intervals_wrapper))
