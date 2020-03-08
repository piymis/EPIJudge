from test_framework import generic_test


def reverse_sublist(L, start, finish):
    # TODO - you fill in here.

    prev_start = node_start = None
    current = L

    node_count = 1

    while node_count < start:
        prev_start = current
        current = current.next
        node_count += 1

    node_start = current

    prev = current
    current = current.next
    
    while node_count < finish:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    prev_start.next = current

    node_start.next = current.next
    return None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
