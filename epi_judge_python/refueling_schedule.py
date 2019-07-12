import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20


# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons, distances):
    # TODO - you fill in here.
    min_city = len(gallons) - 1
    min_gas_level = gallons[-1]

    current_gas_level = gallons[-1] - distances[-1] / MPG

    for i, (refuel_gas, distance) in enumerate(zip(gallons, distances)):
        if current_gas_level < min_gas_level:
            min_gas_level = current_gas_level
            min_city = i

        current_gas_level += refuel_gas - distance / MPG

    return min_city


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("refueling_schedule.py",
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
