from test_framework import generic_test


def search_first_of_k(A, k):
    # TODO - you fill in here.
    def search(a, b):
        m = (a + b) // 2

        if a > b:
            return -1

        if A[m] < k:
            return search(m + 1, b)
        elif A[m] > k:
            return search(a, m - 1)
        else:
            if m == 0 or A[m - 1] != k:
                return m
            else:
                return search(a, m - 1)

    def search_iter(a, b):
        while a <= b:
            m = (a + b) // 2
            if A[m] < k:
                a = m + 1
            elif A[m] > k:
                b = m - 1
            else:
                b = m - 1
                if m == 0 or A[m - 1] != k:
                    return m

        return -1

    # m = search(0, len(A) - 1)
    m = search_iter(0, len(A) - 1)

    return m


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
