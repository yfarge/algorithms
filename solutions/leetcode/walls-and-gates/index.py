from typing import List
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        queue = deque()
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))

        while queue:
            for _ in range(len(queue)):
                row, col, steps = queue.popleft()

                for next_row, next_col in [
                    (row, col - 1),
                    (row - 1, col),
                    (row, col + 1),
                    (row + 1, col),
                ]:
                    if (
                        0 <= next_row < m
                        and 0 <= next_col < n
                        and rooms[next_row][next_col] == INF
                    ):
                        queue.append((next_row, next_col, steps + 1))
                        rooms[next_row][next_col] = steps + 1
