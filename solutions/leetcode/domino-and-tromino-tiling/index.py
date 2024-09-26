# Recursive
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


# Iterative
class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n

        if n == 3:
            return 5

        MOD = 1_000_000_007
        n1, n2, n3 = 5, 2, 1
        for i in range(4, n + 1):
            temp = 2 * n1 + n3
            n2, n3 = n1, n2
            n1 = temp % MOD

        return n1
