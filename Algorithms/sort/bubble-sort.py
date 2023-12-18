import random
from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                swap = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = swap
    return nums


class Test:
    def __init__(self, N) -> None:
        [self.test(10**i) for i in range(N)]

    def test(self, N):
        test_list = [random.randint(-1000, 1000) for _ in range(N)]
        bubble_sorted = bubble_sort(test_list)
        known_sorted = sorted(test_list)
        testPassed = bubble_sorted == known_sorted
        print(f"{"Passed" if testPassed else "Failed"} test {N}")
        assert testPassed


if __name__ == "__main__":
    Test(5)
