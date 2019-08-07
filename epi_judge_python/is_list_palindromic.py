from test_framework import generic_test


def reverse_list(L):
    prev_node, node = None, L

    while node:
        next_node = node.next
        node.next = prev_node
        prev_node = node
        node = next_node

        # prev_node, node, node.next = node, node.next, prev_node

    return prev_node


def is_linked_list_a_palindrome(L):
    # TODO - you fill in here.
    prev_slow, slow, fast = None, L, L
    while fast and fast.next:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next

    L1 = L
    # if prev_slow:
    #     prev_slow.next = None
    L2 = reverse_list(slow)

    while L1 and L2:
        if L1.data != L2.data:
            return False

        L1 = L1.next
        L2 = L2.next

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
