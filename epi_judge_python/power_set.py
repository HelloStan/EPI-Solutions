from test_framework import generic_test, test_utils


def generate_power_set(S):
    # TODO - you fill in here.
    subsets = []
    for i in range(1 << len(S)):
        subset = []
        for j in range(len(S)):
            if i & (1 << j):
                subset.append(S[j])

        subsets.append(subset)

    return subsets


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
