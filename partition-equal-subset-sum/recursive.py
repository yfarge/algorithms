from typing import List
from functools import lru_cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(target: int, n: int):
            if target == 0:
                return True

            if n == 0 or target < 0:
                return False

            return dfs(target - nums[n], n - 1) or dfs(target, n - 1)

        total = sum(nums)
        if total % 2:
            return False

        return dfs(total // 2, len(nums) - 1)
