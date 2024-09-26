from typing import List


# Recursive
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(output: str):
            if output in dp:
                return dp[output]

            if output == s:
                return True

            if output != s[: len(output)]:
                return False

            for word in wordDict:
                dp[output] = dfs(output + word)
                if dp[output]:
                    return True

            return False

        dp = {}
        return dfs("")


# Iterative
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]
