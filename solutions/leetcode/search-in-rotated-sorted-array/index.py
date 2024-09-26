from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        def binary_search(low: int, high: int):
            while low <= high:
                mid = (low + high) // 2

                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    return mid
            return -1

        answer = binary_search(0, left)
        if answer != -1:
            return answer

        return binary_search(left, len(nums) - 1)
