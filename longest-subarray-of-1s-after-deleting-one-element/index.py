from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = deleted = max_length = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                deleted += 1

            while deleted > 1:
                if nums[left] == 0:
                    deleted -= 1
                left += 1

            max_length = max(max_length, right - left)

        return max_length
