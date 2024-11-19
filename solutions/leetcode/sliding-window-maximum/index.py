from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = deque()
        for i in range(k):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        result.append(nums[queue[0]])

        left = 0
        for right in range(k, len(nums)):
            while queue and queue[0] <= left:
                queue.popleft()
            while queue and nums[right] > nums[queue[-1]]:
                queue.pop()
            queue.append(right)
            result.append(nums[queue[0]])
            left += 1

        return result
