from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i):
            if i <= 1:
                return 0

            if i in dp:
                return dp[i]

            dp[i] = min(cost[i - 1] + dfs(i - 1), cost[i - 2] + dfs(i - 2))

            return dp[i]

        dp = {}
        return dfs(len(cost))
