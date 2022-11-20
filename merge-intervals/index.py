from typing import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda i: i[0])
        result = [intervals[0]]

        for start, end in intervals:
            lastEnd = result[-1][1]
            if start <= lastEnd:
                result[-1][1] = max(lastEnd, end)
            else:
                result.append([start, end])

        return result
