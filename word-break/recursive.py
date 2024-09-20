from typing import List


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
