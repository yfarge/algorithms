from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n, k = len(nums), 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k
