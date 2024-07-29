from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations = []

        def backtrack(start: int, path: List[int], seen: List[int]):
            if len(path) == k:
                if sum(path) == n:
                    combinations.append(path.copy())
                return

            for i in range(start, 10):
                if not seen[i - 1]:
                    path.append(i)
                    seen[i - 1] = True
                    backtrack(i, path, seen)
                    path.pop()
                    seen[i - 1] = False

        seen = [False] * 9
        backtrack(1, [], seen)
        return combinations
