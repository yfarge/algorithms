from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum = 0
        current_minimum = 0
        result = nums[0]
        for num in nums:
            running_sum += num
            result = max(result, running_sum - current_minimum)
            if running_sum < current_minimum:
                current_minimum = running_sum

        return result
