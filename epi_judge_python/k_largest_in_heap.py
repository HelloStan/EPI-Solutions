from test_framework import generic_test, test_utils
import heapq


def k_largest_in_binary_heap(A, k):
    # TODO - you fill in here.
    heap = []
    heapq.heappush(heap, (-A[0], 0))

    result = []
    for _ in range(k):
        i = heapq.heappop(heap)[1]

        result.append(A[i])

        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(A):
            heapq.heappush(heap, (-A[left], left))
        if right < len(A):
            heapq.heappush(heap, (-A[right], right))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
