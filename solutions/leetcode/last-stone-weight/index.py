from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapify(heap)

        while len(heap) > 1:
            x, y = heappop(heap), heappop(heap)
            if y > x:
                heappush(heap, x - y)

        return -heap[0] if heap else 0
