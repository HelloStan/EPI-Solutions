from test_framework import generic_test
import heapq


def online_median(sequence):
    # TODO - you fill in here.
    min_heap = []
    max_heap = []

    median = []

    for x in sequence:
        x = heapq.heappushpop(min_heap, x)
        heapq.heappush(max_heap, -x)

        if len(max_heap) > len(min_heap):
            x = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, x)

        x = (min_heap[0] - max_heap[0]) / 2 if len(min_heap) == len(max_heap) else min_heap[0]

        # if len(min_heap) and x > min_heap[0]:
        # else:
        #     heapq.heappush(min_heap, x)

        # while len(min_heap) > len(max_heap):
        #     x = heapq.heappop(min_heap)
        #     heapq.heappush(max_heap, -x)

        # while len(min_heap) < len(max_heap):
        #     x = -heapq.heappop(max_heap)
        #     heapq.heappush(min_heap, x)

        # if len(min_heap) > len(max_heap):
        #     x = min_heap[0]
        # elif len(min_heap) < len(max_heap):
        #     x = -max_heap[0]
        # else:
        #     x = (min_heap[0] - max_heap[0]) / 2

        median.append(x)

    return median


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
