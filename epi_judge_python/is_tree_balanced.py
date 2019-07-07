from test_framework import generic_test


def is_balanced_binary_tree(tree):
    # TODO - you fill in here.
    balanced = True

    def explore(root, depth=0):
        nonlocal balanced

        if not root or not balanced:
            return depth

        depth_left = explore(root.left, depth+1)
        depth_right = explore(root.right, depth+1)

        if abs(depth_left - depth_right) > 1:
            balanced = False

        return max(depth_left, depth_right)

    explore(tree)

    return balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
