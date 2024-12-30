from typing import List
from heapq import heappush, heappop


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, (x, y) in enumerate(points):
            dist = pow(x, 2) + pow(y, 2)
            heappush(heap, (-dist, i))
            if len(heap) > k:
                heappop(heap)

        return [points[i] for _, i in heap]
