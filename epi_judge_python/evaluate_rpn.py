from test_framework import generic_test


def evaluate(expression):
    # TODO - you fill in here.
    operators = {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a // b,
    }

    stack = []
    for tocken in expression.split(','):
        if tocken in operators:
            if len(stack) < 2:
                return False

            B = stack.pop()
            A = stack.pop()
            C = operators[tocken](A, B)

            stack.append(C)
        else:
            if tocken[0] == '-':
                if not tocken[1:].isdigit():
                    return False
            else:
                if not tocken[0:].isdigit():
                    return False

            stack.append(int(tocken))

    if len(stack) == 1:
        return stack[0]

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
