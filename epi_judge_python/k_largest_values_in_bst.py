from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    # TODO - you fill in here.
    k_largest = []

    def traverse(tree):
        if not tree:
            return

        if len(k_largest) >= k:
            return

        traverse(tree.right)

        if len(k_largest) >= k:
            return
        k_largest.append(tree.data)

        traverse(tree.left)

    traverse(tree)

    return k_largest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
