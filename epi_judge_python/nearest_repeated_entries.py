from test_framework import generic_test


def find_nearest_repetition(paragraph):
    # TODO - you fill in here.
    last_positions = {}
    min_distances = {}

    for i, word in enumerate(paragraph):
        if word in last_positions:
            last_position = last_positions[word]

            if word in min_distances:
                min_distances[word] = min(min_distances[word], i - last_position)
            else:
                min_distances[word] = i - last_position

        last_positions[word] = i

    min_distance = min(min_distances.values()) if len(min_distances) else -1

    return min_distance


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
