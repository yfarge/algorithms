from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int, path: List[int]):
            result.append(path.copy())

            for start in range(i, len(nums)):
                path.append(nums[start])
                dfs(start + 1, path)
                path.pop()

        result = []
        dfs(0, [])
        return result
