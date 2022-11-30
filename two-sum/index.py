from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            j = seen.get(target - num)
            if j != None:
                return [j, i]
            seen[num] = i
        return []
