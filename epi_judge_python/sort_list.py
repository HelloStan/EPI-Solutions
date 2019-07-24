from test_framework import generic_test
from list_node import ListNode


def merge_list(a, b):
    head = ListNode(0, None)

    runner = head
    while a and b:
        if a.data < b.data:
            runner.next = a
            a = a.next
        else:
            runner.next = b
            b = b.next

        runner = runner.next

    runner.next = a if a else b

    return head.next


def stable_sort_list(L):
    # TODO - you fill in here.
    if not L or not L.next:
        return L

    pre_slow, slow, fast = None, L, L
    while fast and fast.next:
        pre_slow = slow
        slow = slow.next
        fast = fast.next.next

    pre_slow.next = None

    return merge_list(stable_sort_list(L), stable_sort_list(slow))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_list.py", 'sort_list.tsv',
                                       stable_sort_list))
