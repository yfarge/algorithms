from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(node: int):
            res = node

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]

            return res

        def union(n1: int, n2: int):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += 1
            else:
                par[p2] = p1
                rank[p1] += 1

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return [-1, -1]
