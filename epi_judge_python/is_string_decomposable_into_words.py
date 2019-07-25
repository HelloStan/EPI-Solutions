import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain, dictionary):
    # TODO - you fill in here.
    last_length = [-1] * len(domain)

    for i in range(len(domain)):
        if domain[:i + 1] in dictionary:
            last_length[i] = i + 1

        for j in range(i):
            if last_length[j] > 0 and domain[j + 1: i + 1] in dictionary:
                last_length[i] = i - j
                break

    result = []
    i = len(last_length) - 1
    while i >= 0 and last_length[i] > 0:
        result.append(domain[i - last_length[i] + 1: i + 1])
        i -= last_length[i]

    result = result[::-1]

    return result


def decompose_into_dictionary_words_complex(domain, dictionary):
    # TODO - you fill in here.
    prefix_decompostable = [True] + [False] * len(domain)
    words_at_index = [set() for _ in range(len(prefix_decompostable))]

    domain = ' ' + domain

    for i in range(1, len(domain)):
        for j in range(1, i + 1):
            word = domain[j: i + 1]
            if word in dictionary and prefix_decompostable[i - len(word)]:
                prefix_decompostable[i] = True
                words_at_index[i].add(word)

    def combinations(index, sequence):
        if not prefix_decompostable[index]:
            return False

        if index == 0:
            result.append(sequence[::-1].copy())

        for word in words_at_index[index]:
            combinations(index - len(word), sequence + [word])

    def get_sequence(index, sequence):
        if not prefix_decompostable[index]:
            return

        if index == 0:
            result = sequence[::-1].copy()

        for word in words_at_index[index]:
            combinations(index - len(word), sequence + [word])
            return

    result = []
    # combinations(len(prefix_decompostable) - 1, [])
    get_sequence(len(prefix_decompostable) - 1, [])

    return result[0] if len(result) else []


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_decomposable_into_words.py",
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
