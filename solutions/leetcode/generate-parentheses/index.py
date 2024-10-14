from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(path: List[str], stack: List[str]):
            if len(path) == 2 * n:
                if not stack:
                    result.append("".join(path))
                return

            dfs(path + ["("], stack + [")"])

            if stack and stack[-1] == ")":
                stack.pop()
                dfs(path + [")"], stack)

        result = []
        dfs([], [])
        return result
