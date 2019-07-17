from test_framework import generic_test
from list_node import ListNode


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    # TODO - you fill in here.
    head = ListNode(0, L)

    runner_a = head
    runner_b = head

    for _ in range(k + 1):
        if runner_b is None:
            return None
        runner_b = runner_b.next

    while runner_b:
        runner_a = runner_a.next
        runner_b = runner_b.next

    runner_a.next = runner_a.next.next

    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
