from test_framework import generic_test


def binary_tree_depth_order(tree):
    # TODO - you fill in here.
    if tree is None:
        return []

    result = []

    current_level = [tree]
    while current_level:
        new_level = []

        result.append([])
        for node in current_level:
            result[-1].append(node.data)
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)

        current_level = new_level

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
