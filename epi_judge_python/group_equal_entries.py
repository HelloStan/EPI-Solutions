import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Person = collections.namedtuple('Person', ('age', 'name'))


from collections import defaultdict


def group_by_age(people):
    # TODO - you fill in here.
    counts = defaultdict(int)

    for person in people:
        counts[person.age] += 1

    offset = 0
    age_to_offset = {}

    for age, count in counts.items():
        age_to_offset[age] = offset
        offset += count

    while counts:
        from_age = next(iter(counts))
        from_index = age_to_offset[from_age]

        to_age = people[from_index].age
        to_index = age_to_offset[to_age]

        people[from_index], people[to_index] = people[to_index], people[from_index]

        age_to_offset[to_age] += 1

        counts[to_age] -= 1
        if counts[to_age] == 0:
            del counts[to_age]

    return


@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure('Empty result')

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure('Entry set changed')

    ages = set()
    last_age = people[0]

    for x in people:
        if x.age in ages:
            raise TestFailure('Entries are not grouped by age')
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("group_equal_entries.py",
                                       'group_equal_entries.tsv',
                                       group_by_age_wrapper))
