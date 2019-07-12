from test_framework import generic_test


def levenshtein_distance(A, B):
    # TODO - you fill in here.
    A = ' ' + A
    B = ' ' + B
    D = [[0] * (len(B)) for _ in range(len(A))]

    for i in range(1, len(A)):
        D[i][0] = 1 + D[i-1][0]
    for j in range(1, len(B)):
        D[0][j] = 1 + D[0][j-1]

    for i in range(1, len(A)):
        for j in range(1, len(B)):
            if A[i] == B[j]:
                D[i][j] = D[i-1][j-1]
            else:
                D[i][j] = 1 + min(D[i-1][j-1], D[i-1][j], D[i][j-1])

    return D[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
