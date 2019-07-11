from test_framework import generic_test
import random


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    # TODO - you fill in here.
    def swap(a, b):
        A[a], A[b] = A[b], A[a]

    def partition(a, b, pivot_index):
        pivot = A[pivot_index]

        swap(pivot_index, b)

        pivot_index = a
        for i in range(a, b):
            if A[i] > pivot:
                swap(i, pivot_index)
                pivot_index += 1

        swap(b, pivot_index)

        return pivot_index

    a = 0
    b = len(A) - 1
    while a <= b:
        m = random.randint(a, b)
        pivot_index = partition(a, b, m)

        if pivot_index > k - 1:
            b = pivot_index - 1
        elif pivot_index < k - 1:
            a = pivot_index + 1
        else:
            return A[pivot_index]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
