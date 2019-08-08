from test_framework import generic_test


def longest_contained_range(A):
    # TODO - you fill in here.
    entries = set(A)

    largest_set = 0
    while entries:
        x = entries.pop()

        lower_bound = x
        while lower_bound - 1 in entries:
            lower_bound -= 1
            entries.remove(lower_bound)

        upper_bound = x
        while upper_bound + 1 in entries:
            upper_bound += 1
            entries.remove(upper_bound)

        largest_set = max(largest_set, upper_bound - lower_bound + 1)

    return largest_set


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
