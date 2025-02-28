from typing import List
from heapq import heappush, heappop


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        maxHeap = []
        n = len(grid)

        for i in range(n):
            grid[i].sort(reverse=True)
            for j in range(limits[i]):
                heappush(maxHeap, grid[i][j])
                if len(maxHeap) > k:
                    heappop(maxHeap)

        return sum(maxHeap)
