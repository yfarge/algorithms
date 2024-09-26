from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        i_rep = self.find(i)
        j_rep = self.find(j)

        if i_rep == j_rep:
            return

        if self.rank[i_rep] < self.rank[j_rep]:
            self.parent[i_rep] = j_rep
        elif self.rank[j_rep] < self.rank[i_rep]:
            self.parent[j_rep] = i_rep
        else:
            self.parent[i_rep] = j_rep
            self.rank[i_rep] += 1
        self.parent[i_rep] = j_rep


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = result = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] and uf.find(i) != uf.find(j):
                    uf.union(i, j)
                    result -= 1

        return result
