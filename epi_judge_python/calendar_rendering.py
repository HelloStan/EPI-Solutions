import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


def find_max_simultaneous_events(A):
    # TODO - you fill in here.
    events = [
            p
            for event in A
            for p in [Endpoint(event.start, True), Endpoint(event.finish, False)]
        ]

    events.sort(key=lambda e: (e.time, 0 if e.is_start else 1))

    counter = 0
    counter_max = 0
    for time, is_start in events:
        if is_start:
            counter += 1
            counter_max = max(counter_max, counter)
        else:
            counter -= 1

    return counter_max


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
