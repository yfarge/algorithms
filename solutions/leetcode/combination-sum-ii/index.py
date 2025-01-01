from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, path = [], []

        def backtrack(start: int, currentTarget: int):
            if currentTarget == 0:
                res.append(path.copy())
                return

            if currentTarget < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, currentTarget - candidates[i])
                path.pop()

        backtrack(0, target)
        return res
