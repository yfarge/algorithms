from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 0
        maxIncreasing = maxDecreasing = 0
        for i in range(len(nums) - 1):
            isIncreasing = nums[i] < nums[i + 1]
            isDecreasing = nums[i] > nums[i + 1]

            maxIncreasing = maxIncreasing * isIncreasing + isIncreasing
            maxDecreasing = maxDecreasing * isDecreasing + isDecreasing

            res = max(res, maxDecreasing, maxIncreasing)

        return res + 1
