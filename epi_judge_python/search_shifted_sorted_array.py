from test_framework import generic_test


def search_smallest(A):
    # TODO - you fill in here.
    a = 0
    b = len(A) - 1

    while a < b:
        m = (a + b) // 2

        if A[m] > A[b]:
            a = m + 1
        else:
            b = m

    return b


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
