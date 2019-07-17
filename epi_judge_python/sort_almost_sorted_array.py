from test_framework import generic_test
import heapq


def sort_approximately_sorted_array(sequence, k):
    # TODO - you fill in here.
    heap = []
    sorted_array = []

    for x in sequence:
        if len(heap) == k:
            sorted_array.append(heapq.heappop(heap))

        heapq.heappush(heap, x)

    while heap:
        sorted_array.append(heapq.heappop(heap))

    return sorted_array


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
