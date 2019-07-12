from test_framework import generic_test
from collections import deque
import string


# Uses BFS to find the least steps of transformation.
def transform_string(D, s, t):
    # TODO - you fill in here.
    queue = deque()

    queue.append((0, s))
    D.remove(s)

    while queue:
        dist, word = queue.popleft()

        for i in range(len(word)):
            for c in string.ascii_lowercase:
                new_word = word[:i] + c + word[i+1:]

                if new_word in D:
                    D.remove(new_word)
                    queue.append((dist + 1, new_word))

                    if new_word == t:
                        return dist + 1

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
