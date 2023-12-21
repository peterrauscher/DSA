from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                swap = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = swap
    return nums
