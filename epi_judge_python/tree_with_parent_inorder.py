from test_framework import generic_test


def inorder_traversal(tree):
    # TODO - you fill in here.
    traversal = []

    last_node = None
    while tree:
        if last_node is tree.parent:
            if not tree.left:
                traversal.append(tree.data)
            next_node = tree.left or tree.right or tree.parent
        elif last_node is tree.left:
            traversal.append(tree.data)
            next_node = tree.right or tree.parent
        else:
            next_node = tree.parent

        last_node = tree
        tree = next_node
    return traversal


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
