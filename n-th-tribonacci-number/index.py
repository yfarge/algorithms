class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}

        def dfs(n: int) -> int:
            if n in memo:
                return memo[n]

            memo[n] = dfs(n - 1) + dfs(n - 2) + dfs(n - 3)
            return memo[n]

        return dfs(n)
