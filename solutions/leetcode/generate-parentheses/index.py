from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(o: int, c: int):
            if o == c == n:
                result.append("".join(path))
                return

            if o < n:
                path.append('(')
                backtrack(o + 1, c)
                path.pop()

            if c < o:
                path.append(')')
                backtrack(o, c + 1)
                path.pop()

        result, path = [], []
        backtrack(0, 0)
        return result
