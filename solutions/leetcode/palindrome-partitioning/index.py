from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []

        def backtrack(i: int):
            if i >= len(s):
                res.append(path.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    path.append(s[i: j + 1])
                    backtrack(j + 1)
                    path.pop()

        backtrack(0)
        return res

    def isPalindrome(self, s: str, i: int, j: int) -> bool:
        left = i
        right = j

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
