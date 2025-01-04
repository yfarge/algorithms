from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def bfs(i: int, j: int):
            queue = deque([(i, j)])
            area = 0

            while queue:
                row, col = queue.popleft()
                if grid[row][col] == 2:
                    continue

                grid[row][col] = 2
                area += 1

                for next_row, next_col in [
                    (row, col - 1),
                    (row - 1, col),
                    (row, col + 1),
                    (row + 1, col),
                ]:
                    if (
                        0 <= next_row < m
                        and 0 <= next_col < n
                        and grid[next_row][next_col] == 1
                    ):
                        queue.append((next_row, next_col))

            return area

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, bfs(i, j))

        return res
