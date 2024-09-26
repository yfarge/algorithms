from functools import cache


# Recursive
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        @cache
        def dfs(i: int, j: int):
            if i >= m:
                return len(word2) - j

            if j >= n:
                return len(word1) - i

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            return 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))

        return dfs(0, 0)


# Iterative
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][n] = m - i

        for j in range(n + 1):
            dp[m][j] = n - j

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i]
                                       [j + 1], dp[i + 1][j + 1])

        return dp[0][0]
