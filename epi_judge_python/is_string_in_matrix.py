from test_framework import generic_test


def is_pattern_contained_in_grid(grid, S):
    # TODO - you fill in here.
    def is_valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    failed_suffixes = set()  # (x, y, offset)

    def is_suffix_found(x, y, offset):
        if offset == len(S):
            return True

        if not is_valid(x, y):
            return False
        if grid[x][y] != S[offset]:
            return False
        if (x, y, offset) in failed_suffixes:
            return False

        for dx, dy in [(0, -1), (0, +1), (-1, 0), (+1, 0)]:
            if is_suffix_found(x + dx, y + dy, offset + 1):
                return True

        failed_suffixes.add((x, y, offset))
        return False

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if is_suffix_found(x, y, 0):
                return True

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
