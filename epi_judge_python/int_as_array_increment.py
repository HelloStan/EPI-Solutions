from test_framework import generic_test


def plus_one(A):
    # TODO - you fill in here.
    carry = 1
    for i in reversed(range(len(A))):
        A[i] += carry
        carry = A[i] // 10
        A[i] %= 10

    if carry:
        A.insert(0, carry)

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
