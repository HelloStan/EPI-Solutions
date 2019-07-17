from test_framework import generic_test


def number_of_ways(n, m):
    # TODO - you fill in here.
    grid = [[0]*m for _ in range(n)]

    for i in range(n):
        grid[i][0] = 1
    for j in range(m):
        grid[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]

    return grid[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
