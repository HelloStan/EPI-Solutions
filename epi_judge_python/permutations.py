from test_framework import generic_test, test_utils


def permutations(A):
    # TODO - you fill in here.
    def gen_permutations(k):
        if k == 0:
            permutations.append(A.copy())
            return

        for i in range(0, k + 1):
            A[i], A[k] = A[k], A[i]
            gen_permutations(k - 1)
            A[i], A[k] = A[k], A[i]

    permutations = []
    gen_permutations(len(A) - 1)

    return permutations


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
