from test_framework import generic_test


def has_two_sum(A, t):
    # TODO - you fill in here.
    i, j = 0, len(A) - 1

    while i <= j:
        if A[i] + A[j] < t:
            i += 1
        elif A[i] + A[j] > t:
            j -= 1
        else:
            return True

    return False


def has_three_sum(A, t):
    # TODO - you fill in here.
    A.sort()
    for v in A:
        if has_two_sum(A, t - v):
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
