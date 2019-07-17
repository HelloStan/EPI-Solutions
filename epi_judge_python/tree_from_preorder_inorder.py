from test_framework import generic_test
from binary_tree_node import BinaryTreeNode

def binary_tree_from_preorder_inorder(preorder, inorder):
    # TODO - you fill in here.
    inorder_node_to_index = {}
    for i, node in enumerate(inorder):
        inorder_node_to_index[node] = i

    def build_tree(preorder_a, preorder_b, inorder_a, inorder_b):
        if preorder_a > preorder_b or inorder_a > inorder_b:
            return None

        inorder_root_index = inorder_node_to_index[preorder[preorder_a]]
        left_size = inorder_root_index - inorder_a

        root_data = preorder[preorder_a]

        left_leaf = build_tree(preorder_a + 1,
                               preorder_a + left_size,
                               inorder_a,
                               inorder_root_index - 1)
        right_leaf = build_tree(preorder_a + 1 + left_size,
                                preorder_b,
                                inorder_root_index + 1,
                                inorder_b)

        root = BinaryTreeNode(root_data, left_leaf, right_leaf)

        return root

    return build_tree(0, len(preorder) - 1, 0, len(inorder) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
