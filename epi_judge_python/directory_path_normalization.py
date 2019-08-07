from test_framework import generic_test


def shortest_equivalent_path(path):
    # TODO - you fill in here.
    is_absolute = path[0] == '/'
    path = path.split('/')

    stack = []

    for token in path:
        if token == '.' or len(token) == 0:
            continue
        elif token == '..':
            if len(stack) > 0 and stack[-1] != '..':
                stack.pop()
            else:
                stack.append(token)
        else:
            stack.append(token)

    path = '/'.join(stack)

    if is_absolute:
        path = '/' + path

    return path


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
