from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    # TODO - you fill in here.
    for i in range(9):
        row_set = set()
        col_set = set()

        for j in range(9):
            if partial_assignment[i][j] in row_set:
                return False
            if partial_assignment[j][i] in col_set:
                return False

            if partial_assignment[i][j] != 0:
                row_set.add(partial_assignment[i][j])
            if partial_assignment[j][i] != 0:
                col_set.add(partial_assignment[j][i])

    for k in range(0, 9, 3):
        for l in range(0, 9, 3):
            block_set = set()

            for i in range(k, k + 3):
                for j in range(l, l + 3):
                    if partial_assignment[i][j] in block_set:
                        return False

                    if partial_assignment[i][j] != 0:
                        block_set.add(partial_assignment[i][j])

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
