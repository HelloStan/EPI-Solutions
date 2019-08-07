import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


from binary_tree_node import BinaryTreeNode


def reconstruct_preorder(preorder):
    # TODO - you fill in here.
    def build_tree(iterator):
        key = next(iterator)
        if key is None:
            return None

        left = build_tree(iterator)
        right = build_tree(iterator)

        return BinaryTreeNode(key, left, right)

    return build_tree(iter(preorder))


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_with_null.py",
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
