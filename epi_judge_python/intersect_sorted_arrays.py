from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    # TODO - you fill in here.
    i = 0
    j = 0

    intersection = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            if len(intersection) == 0 or intersection[-1] != A[i]:
                intersection.append(A[i])
            i += 1
            j += 1

    return intersection


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
