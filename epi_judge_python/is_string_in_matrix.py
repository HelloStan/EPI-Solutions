from test_framework import generic_test


def is_pattern_contained_in_grid(grid, S):
    # TODO - you fill in here.
    def is_valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    prev_valid = [[True]*len(grid[0]) for _ in range(len(grid))]

    for v in S:
        current_valid = [[False]*len(grid[0]) for _ in range(len(grid))]
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == v:
                    for dx, dy in [(0, -1), (0, +1), (-1, 0), (+1, 0)]:
                        nx, ny = x + dx, y + dy
                        if is_valid(nx, ny) and prev_valid[nx][ny]:
                            current_valid[x][y] = True
                        if len(S) == 1:
                            current_valid[x][y] = True

        prev_valid = current_valid

    return max([max(row) for row in prev_valid])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
