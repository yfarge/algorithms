from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path: List[int]):
            if len(path) == len(nums):
                answer.append(path.copy())

            for num in nums:
                if num in seen:
                    continue
                seen.add(num)
                path.append(num)
                dfs(path)
                path.pop()
                seen.discard(num)

        answer = []
        seen = set()
        dfs([])
        return answer
