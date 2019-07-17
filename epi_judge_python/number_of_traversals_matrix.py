from test_framework import generic_test


def number_of_ways(n, m):
    # TODO - you fill in here.
    if m > n:
        n, m = m, n

    row = [1] * m

    for i in range(1, n):
        new_row = row.copy()
        for j in range(1, m):
            new_row[j] = new_row[j-1] + row[j]

        row = new_row

    return row[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
