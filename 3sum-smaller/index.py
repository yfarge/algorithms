from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n):
            left, right = i + 1, n - 1

            while left < right:
                total = nums[left] + nums[right] + nums[i]

                if total < target:
                    count += right - left
                    left += 1
                elif total >= target:
                    right -= 1
        return count
