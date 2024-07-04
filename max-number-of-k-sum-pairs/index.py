from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i, j = 0, len(nums) - 1
        sorted_nums = sorted(nums)
        pairs = 0
        while i < j:
            s = sorted_nums[i] + sorted_nums[j]
            if s < k:
                i += 1
            elif s > k:
                j -= 1
            else:
                pairs += 1
                i += 1
                j -= 1
        return pairs
