class Solution:
    def numTilings(self, n: int) -> int:
        def dfs(i: int):
            if i <= 0:
                return 0

            if i in dp:
                return dp[i]

            dp[i] = (2 * dfs(i - 1) + dfs(i - 3)) % MOD
            return dp[i]

        MOD = 1_000_000_007
        dp = {1: 1, 2: 2, 3: 5}
        return dfs(n)
