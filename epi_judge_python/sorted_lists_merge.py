from test_framework import generic_test
from list_node import ListNode


def merge_two_sorted_lists(L1, L2):
    # TODO - you fill in here.
    head = dummy_head = ListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            dummy_head.next = L1
            L1 = L1.next
        else:
            dummy_head.next = L2
            L2 = L2.next

        dummy_head = dummy_head.next
    
    dummy_head.next = L1 or L2

    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
