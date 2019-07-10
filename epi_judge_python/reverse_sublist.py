from test_framework import generic_test
from list_node import ListNode


def reverse_sublist(L, start, finish):
    # TODO - you fill in here.
    if L is None or start == finish:
        return L

    # Get to start position
    parent = None
    runner = L
    for _ in range(1, start):
        parent = runner
        runner = runner.next

    def reverse_sublist(parent, runner, count):
        for i in range(count):
            runner_next = runner.next
            runner.next = parent

            parent, runner = runner, runner_next

        return parent, runner

    head, ne = reverse_sublist(parent, runner, finish - start + 1)

    if parent:
        parent.next = head
    else:
        L = head
    runner.next = ne

    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
