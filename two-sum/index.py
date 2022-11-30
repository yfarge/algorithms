from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            j = d.get(target - num)
            if j != None:
                return [j, i]
            d[num] = i
        return []
