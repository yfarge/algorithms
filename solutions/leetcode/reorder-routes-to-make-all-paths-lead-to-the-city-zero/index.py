from typing import List
from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)
        for a, b in connections:
            adjacency_list[a].append((b, True))
            adjacency_list[b].append((a, False))

        count = 0
        seen = [False] * n
        stack = [(0, False)]

        while stack:
            node, direction = stack.pop()
            if not seen[node]:
                seen[node] = True
                count += direction
                for neighbor, direction in adjacency_list[node]:
                    stack.append((neighbor, direction))

        return count
