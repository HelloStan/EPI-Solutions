from test_framework import generic_test
from copy import copy


def n_queens(n):
    # TODO - you fill in here.
    solution = []
    row_placements = [-1] * n

    row_spaces = set()
    diag_a_spaces = set()
    diag_b_spaces = set()

    def solve(col=0):
        if col == n:
            solution.append(copy(row_placements))
            return

        for row in range(n):
            if row in row_spaces:
                continue
            if (col - row) in diag_a_spaces:
                continue
            if (n - row - col - 1) in diag_b_spaces:
                continue

            row_spaces.add(row)
            diag_a_spaces.add((col - row))
            diag_b_spaces.add((n - row - col - 1))

            row_placements[col] = row
            solve(col + 1)

            row_spaces.remove(row)
            diag_a_spaces.remove((col - row))
            diag_b_spaces.remove((n - row - col - 1))

    solve()

    return solution


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))
