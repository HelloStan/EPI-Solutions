from test_framework import generic_test


def look_and_say(n):
    # TODO - you fill in here.
    def next_string(s):
        say_s = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1

            say_s.append(str(j - i))
            say_s.append(s[i])
            i = j

        return ''.join(say_s)

    s = '1'
    for i in range(n - 1):
        s = next_string(s)

    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
