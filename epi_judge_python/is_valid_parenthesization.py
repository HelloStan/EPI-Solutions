from test_framework import generic_test


def is_well_formed(s):
    # TODO - you fill in here.
    stack = []

    for c in s:
        if c not in "(){}[]":
            return False

        if c in "({[":
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            if c == ')' and stack[-1] != '(':
                return False
            if c == '}' and stack[-1] != '{':
                return False
            if c == ']' and stack[-1] != '[':
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
