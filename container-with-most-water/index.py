from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        max_height = max(height)
        while l < r:
            area = max((r - l) * min(height[l], height[r]), area)
            if max_height * (r - l) < area:
                break
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area
