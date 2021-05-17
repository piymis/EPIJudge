from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    # TODO - you fill in here.

    def compute_permutations(nums: List[int]):
        if len(nums) <= 1:
            return [nums]

        result = []
        for i, num in enumerate(nums):
            result += [[num] + x for x in compute_permutations(nums[:i] + nums[i+1:])]

        return result

    return compute_permutations(A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
