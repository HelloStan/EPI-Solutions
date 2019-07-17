from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity):
        # TODO - you fill in here.
        self.array = [0] * capacity
        self.head = 0
        self.tail = 0
        self.num_elements = 0

    def enqueue(self, x):
        # TODO - you fill in here.
        if self.num_elements == len(self.array):
            self.array = self.array[self.tail:] + self.array[:self.head] + [0] * len(self.array)
            self.tail = 0
            self.head = self.num_elements

        self.array[self.head] = x
        self.head = (self.head + 1) % len(self.array)

        self.num_elements += 1

    def dequeue(self):
        # TODO - you fill in here.
        x = self.array[self.tail]
        self.tail = (self.tail + 1) % len(self.array)
        self.num_elements -= 1
        return x

    def size(self):
        # TODO - you fill in here.
        return self.num_elements


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
