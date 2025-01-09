from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        minHeap = [(0, k)]
        visited = set()
        res = 0
        while minHeap:
            wu, u = heappop(minHeap)
            if u in visited:
                continue
            visited.add(u)
            res = max(res, wu)

            for v, wv in graph[u]:
                if v not in visited:
                    heappush(minHeap, (wu + wv, v))

        return res if len(visited) == n else -1
