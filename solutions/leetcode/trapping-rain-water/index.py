from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max, right_max = [0] * n, [0] * n

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i - 1])

        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i + 1])

        result = 0

        for i in range(n):
            result += max(min(left_max[i], right_max[i]) - height[i], 0)
        return result
