from test_framework import generic_test


def can_reach_end(A):
    # TODO - you fill in here.
    furthest_reached_so_far = 0
    last_index = len(A) - 1
    i = 0

    while i <= furthest_reached_so_far and furthest_reached_so_far < last_index:
        furthest_reached_so_far = max(furthest_reached_so_far, A[i] + i)
        i += 1
    return furthest_reached_so_far >= last_index



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
