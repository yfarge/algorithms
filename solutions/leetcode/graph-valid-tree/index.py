from typing import List
from collections import defaultdict, deque


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        queue = deque([(0, -1)])
        visited = set([0])

        while queue:
            node, parent = queue.popleft()

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                if neighbor in visited:
                    return False

                visited.add(neighbor)
                queue.append((neighbor, node))

        return len(visited) == n
