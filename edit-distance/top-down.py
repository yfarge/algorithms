from functools import cache


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
