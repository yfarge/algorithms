from typing import List, Dict
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path: List[int], counter: Dict[int, int]):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in counter:
                if counter[num] > 0:
                    path.append(num)
                    counter[num] -= 1
                    backtrack(path, counter)
                    counter[num] += 1
                    path.pop()

        backtrack([], Counter(nums))
        return res
