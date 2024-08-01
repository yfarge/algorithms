from typing import List
from operator import itemgetter


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=itemgetter(1))
        n = len(points)
        arrows = i = 0

        while i < n:
            arrows += 1
            x = points[i][1]
            while i < n and points[i][0] <= x:
                i += 1

        return arrows
