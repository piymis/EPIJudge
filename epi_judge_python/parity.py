from test_framework import generic_test


def parity(x: int) -> int:
    # TODO - you fill in here.
    # Repeatedly erasing the set bit and saving the result mod 2
    result = 0

    while x:
        x &= x-1
        result ^= 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))