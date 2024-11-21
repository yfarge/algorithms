from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        res = nums[0]
        while low <= high:
            if nums[low] < nums[high]:
                res = min(res, nums[low])
                break

            mid = low + (high - low) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        return res
