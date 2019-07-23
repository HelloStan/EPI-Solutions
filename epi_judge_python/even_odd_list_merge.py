from test_framework import generic_test
from list_node import ListNode


def even_odd_merge(L):
    # TODO - you fill in here.
    even_head = ListNode(0, None)
    odd_head = ListNode(0, None)

    even_runner = even_head
    odd_runner = odd_head

    even = False
    while L:
        if even:
            even_runner.next = L
            even_runner = even_runner.next
        else:
            odd_runner.next = L
            odd_runner = odd_runner.next

        L = L.next
        even = not even

    odd_runner.next = even_head.next
    even_runner.next = None

    return odd_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
