from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curr_sum = max_sum = sum(nums[0:k])
        for i in range(n - k):
            curr_sum = curr_sum - nums[i] + nums[i + k]
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum / k
