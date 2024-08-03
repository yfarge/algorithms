class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dfs(i: int, j: int):
            if i >= m or j >= n:
                return 0

            if dp[i][j] is not None:
                return dp[i][j]

            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)

            dp[i][j] = max(dfs(i + 1, j), dfs(i, j + 1))
            return dp[i][j]

        m, n = len(text1), len(text2)
        dp = [[None for _ in range(n)] for _ in range(m)]
        return dfs(0, 0)
