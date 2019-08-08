from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs):
    # TODO - you fill in here.
    def generate(left_needed, right_needed, prefix=""):
        if left_needed > 0:
            generate(left_needed - 1, right_needed, prefix + "(")

        if right_needed > left_needed:
            generate(left_needed, right_needed - 1, prefix + ")")

        if left_needed == 0 and right_needed == 0:
            result.append(prefix)

    result = []
    generate(num_pairs, num_pairs)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_balanced_parentheses.py",
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
