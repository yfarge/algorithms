from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            visited[i] = True
            for j in range(n):
                if isConnected[i][j] and not visited[j]:
                    dfs(j)

        n = len(isConnected)
        visited = [False] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)

        return count
