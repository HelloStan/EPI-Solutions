import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK, VISITED = range(3)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, s, e):
    # TODO - you fill in here.
    def is_valid_location(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == WHITE

    def explore(x, y):
        if not is_valid_location(x, y):
            return False
        maze[x][y] = VISITED

        if x == e.x and y == e.y:
            return True

        for dx, dy in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
            new_x, new_y = x + dx, y + dy

            if explore(new_x, new_y):
                path.append(Coordinate(new_x, new_y))
                return True

        return False

    path = []
    explore(s.x, s.y)

    path.append(s)
    path = list(reversed(path))

    if path[-1] != e:
        return []

    return path


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))
