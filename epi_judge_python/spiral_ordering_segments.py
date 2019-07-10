from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    # TODO - you fill in here.
    n = len(square_matrix)

    spiral = []
    for offset in range(n // 2):
        end = n - 1 - offset

        for i in range(offset, end):
            spiral.append(square_matrix[offset][i])
        for i in range(offset, end):
            spiral.append(square_matrix[i][end])

        for i in range(end, offset, -1):
            spiral.append(square_matrix[end][i])
        for i in range(end, offset, -1):
            spiral.append(square_matrix[i][offset])

    if n % 2:
        spiral.append(square_matrix[n // 2][n // 2])

    return spiral


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
