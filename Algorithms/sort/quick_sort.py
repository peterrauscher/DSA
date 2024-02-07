from typing import List


def quicksort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
