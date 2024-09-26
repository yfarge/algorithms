from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right and nums[left] <= nums[left + 1]:
            left += 1

        while right > 0 and nums[right - 1] <= nums[right]:
            right -= 1

        sub_min, sub_max = float('inf'), float('-inf')

        for i in range(left, right + 1):
            sub_min = min(sub_min, nums[i])
            sub_max = max(sub_max, nums[i])

        while left > 0 and nums[left - 1] > sub_min:
            left -= 1

        while right < len(nums) - 1 and nums[right + 1] < sub_max:
            right += 1

        if right <= left:
            return 0

        return right - left + 1
