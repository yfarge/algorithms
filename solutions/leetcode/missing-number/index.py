from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = sum(range(len(nums) + 1))
        for num in nums:
            result -= num
        return result
