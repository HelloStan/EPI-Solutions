from test_framework import generic_test


def is_symmetric(tree):
    # TODO - you fill in here.
    def traverse(left, right):
        if left is None and right is None:
            return True

        if left and right:
            if left.data == right.data and traverse(left.left, right.right) and traverse(left.right, right.left):
                return True

        return False

    return traverse(tree.left, tree.right) if tree else True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
