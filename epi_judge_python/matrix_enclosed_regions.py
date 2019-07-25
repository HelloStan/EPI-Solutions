from test_framework import generic_test


def fill_surrounded_regions(board):
    # TODO - you fill in here.
    n = len(board)
    m = len(board[0])

    def is_valid_point(x, y):
        return 0 <= x < n and 0 <= y < m and board[x][y] == 'W'

    def explore(x, y):
        if not is_valid_point(x, y):
            return

        board[x][y] = 'R'

        for dx, dy in [(0, -1), (0, +1), (-1, 0), (+1, 0)]:
            explore(x + dx, y + dy)

    for i in range(n):
        explore(i, 0)
        explore(i, m - 1)

    for j in range(m):
        explore(0, j)
        explore(n - 1, j)

    for x in range(n):
        for y in range(m):
            board[x][y] = 'W' if board[x][y] == 'R' else 'B'

    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
