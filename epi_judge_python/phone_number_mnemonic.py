from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number):
    # TODO - you fill in here.
    mapping = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

    mnemonics = []
    mnemonic = []

    def func(offset=0):
        if offset == len(phone_number):
            mnemonics.append(''.join(mnemonic))
            return

        digit = phone_number[offset]
        digit = int(digit)
        for letter in mapping[digit]:
            mnemonic.append(letter)
            func(offset + 1)
            mnemonic.pop()

    func()

    return mnemonics


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
