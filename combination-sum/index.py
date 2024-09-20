from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(current_target: int, path: List[int], start: int):
            if current_target == 0:
                answer.append(path.copy())
                return

            if current_target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(current_target - candidates[i], path, i)
                path.pop()

        answer = []
        dfs(target, [], 0)
        return answer
