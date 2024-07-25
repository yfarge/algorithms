from typing import List
from heapq import heappush, heappop


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        min_heap = []
        for i in range(candidates):
            heappush(min_heap, (costs[i], 0))

        for i in range(max(candidates, len(costs) - candidates), len(costs)):
            heappush(min_heap, (costs[i], 1))

        total = 0
        l, r = candidates, len(costs) - 1 - candidates
        for _ in range(k):
            cost, section = heappop(min_heap)
            total += cost

            if l <= r:
                if section == 0:
                    heappush(min_heap, (costs[l], 0))
                    l += 1
                else:
                    heappush(min_heap, (costs[r], 1))
                    r -= 1

        return total
