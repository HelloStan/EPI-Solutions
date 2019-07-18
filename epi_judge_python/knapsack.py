import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    # TODO - you fill in here.
    v = [[0] * (capacity + 1) for _ in items + [0]]

    for i in range(1, len(items) + 1):
        for c in range(1, capacity + 1):
            item = items[i - 1]
            if item.weight <= c:
                v[i][c] = max(v[i - 1][c], v[i - 1][c - item.weight] + item.value)
            else:
                v[i][c] = v[i - 1][c]

    return max(v[-1])


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
