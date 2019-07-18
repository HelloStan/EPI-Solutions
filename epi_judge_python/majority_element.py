from test_framework import generic_test


def majority_search(stream):
    # TODO - you fill in here.
    majority = next(stream)
    count = 1

    for element in stream:
        if count == 0:
            majority = element
            count = 1
        else:
            count += +1 if majority == element else -1

    return majority


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
