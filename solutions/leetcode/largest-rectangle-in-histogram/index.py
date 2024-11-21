from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []
        for current_index, current_height in enumerate(heights):
            start = current_index
            while stack and stack[-1][1] > current_height:
                previous_index, previous_height = stack.pop()
                result = max(result, previous_height *
                             (current_index - previous_index))
                start = previous_index
            stack.append((start, current_height))

        for index, height in stack:
            result = max(result, height * (len(heights) - index))
        return result
