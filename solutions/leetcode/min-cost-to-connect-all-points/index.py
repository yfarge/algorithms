from typing import List
from operator import itemgetter


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        root = [i for i in range(n)]
        rank = [1] * n

        def find(node: int) -> int:
            res = node

            while res != root[res]:
                root[res] = root[root[res]]
                res = root[res]

            return res

        def union(n1: int, n2: int) -> bool:
            r1, r2 = find(n1), find(n2)

            if r1 == r2:
                return False

            if rank[r2] > rank[r1]:
                root[r1] = r2
                rank[r2] += 1
            else:
                root[r2] = r1
                rank[r1] += 1

            return True

        edges = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    w = (
                        abs(points[i][0] - points[j][0]) +
                        abs(points[i][1] - points[j][1])
                    )
                    edges.append((i, j, w))

        edges.sort(key=itemgetter(2))

        res = 0
        for a, b, w in edges:
            if union(a, b):
                res += w

        return res
