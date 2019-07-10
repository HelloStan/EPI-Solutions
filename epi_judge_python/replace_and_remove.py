import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    # TODO - you fill in here.
    j = len(s) - 1
    for i in range(size - 1, -1, -1):
        if s[i] != 'b':
            s[j] = s[i]
            j -= 1

    j += 1
    i = 0
    while j < len(s):
        if s[j] == 'a':
            s[i:i+2] = "dd"
            i += 2
        else:
            s[i] = s[j]
            i += 1
        j += 1

    return i


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
