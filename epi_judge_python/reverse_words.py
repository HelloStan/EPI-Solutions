import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    # TODO - you fill in here.
    def reverse(a, b):
        i = a
        j = b
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    reverse(0, len(s) - 1)

    start = 0
    for i in range(len(s)):
        if s[i] == ord(' '):
            reverse(start, i - 1)
            start = i + 1

    reverse(start, len(s) - 1)

    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
