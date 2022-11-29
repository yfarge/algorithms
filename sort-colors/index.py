from typing import *


def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = 0
    r = len(nums) - 1
    i = 0
    while i < len(nums) and l <= r and i <= r:
        if nums[i] == 0:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
            i += 1
        elif nums[i] == 2:
            nums[r], nums[i] = nums[i], nums[r]
            r -= 1
        else:
            i += 1


nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)
