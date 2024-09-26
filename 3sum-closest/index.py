from typing import List
import sys


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        minimum_distance, minimum_sum = sys.maxsize, sys.maxsize
        for i in range(n):
            left, right = i + 1, n - 1
            pair_target = target - nums[i]

            while left < right:
                pair_sum = nums[left] + nums[right]
                pair_distance = abs(pair_target - pair_sum)
                if pair_distance < minimum_distance:
                    minimum_distance = pair_distance
                    minimum_sum = pair_sum + nums[i]

                if pair_sum < pair_target:
                    left += 1
                elif pair_sum > pair_target:
                    right -= 1
                else:
                    return pair_sum + nums[i]
        return minimum_sum
