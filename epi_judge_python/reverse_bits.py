from test_framework import generic_test


def reverse_byte(x):
    rev = 0
    for i in range(8):
        rev = (rev << 1) | (x & 1)
        x >>= 1
    return rev


reverse_lookup = None


def reverse_bits(x):
    # TODO - you fill in here.

    global reverse_lookup
    if reverse_lookup is None:
        reverse_lookup = [reverse_byte(x) for x in range(256)]

    rev = 0
    for i in range(8):
        rev = (rev << 8) | reverse_lookup[x & 0xFF]
        x >>= 8

    return rev


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
