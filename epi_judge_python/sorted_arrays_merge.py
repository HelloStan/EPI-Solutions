from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    # TODO - you fill in here.
    heap = [(array[0], i, 0) for i, array in enumerate(sorted_arrays)]
    heapq.heapify(heap)

    array = []
    while heap:
        val, i, j = heapq.heappop(heap)
        
        array.append(val)

        j += 1
        if j < len(sorted_arrays[i]):
            heapq.heappush(heap, (sorted_arrays[i][j], i, j))

    return array


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
