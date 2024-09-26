from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i: int):
            if i >= len(nums):
                return 0

            if i in dp:
                return dp[i]

            dp[i] = max(dfs(i + 1), dfs(i + 2) + nums[i])

            return dp[i]

        dp = {}
        return dfs(0)
