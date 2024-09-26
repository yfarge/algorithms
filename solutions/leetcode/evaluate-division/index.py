from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)

        for (u, v), value in zip(equations, values):
            graph[u][v] = value
            graph[v][u] = 1.0 / value

        def dfs(u: int, v: int, visited: set):
            if u not in graph or v not in graph:
                return -1.0
            if v in graph[u]:
                return graph[u][v]
            for neighbor in graph[u]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    result = dfs(neighbor, v, visited)
                    if result != -1:
                        return result * graph[u][neighbor]
            return -1.0

        result = []
        for x, y in queries:
            result.append(dfs(x, y, set()))

        return result
