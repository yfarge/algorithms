from typing import List
from operator import itemgetter


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=itemgetter(1))
        count = 0
        i, j = 0, 1
        while i < len(intervals) and j < len(intervals):
            a, b = intervals[i], intervals[j]
            if a[0] < b[1] and b[0] < a[1]:
                count += 1
                j += 1
            else:
                i = j
                j = i + 1
        return count
