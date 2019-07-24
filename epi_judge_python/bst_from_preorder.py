from test_framework import generic_test
from bst_node import BstNode


def rebuild_bst_from_preorder(preorder_sequence):
    # TODO - you fill in here.
    def build_bst(lower_bound=-float('inf'), upper_bound=+float('inf')):
        nonlocal root_idx

        if root_idx >= len(preorder_sequence):
            return None

        root = preorder_sequence[root_idx]
        if not lower_bound < root < upper_bound:
            return None

        root_idx += 1

        left = build_bst(lower_bound, root)
        right = build_bst(root, upper_bound)

        return BstNode(root, left, right)

    root_idx = 0
    return build_bst()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
