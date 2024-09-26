from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, columns = len(maze), len(maze[0])
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        while queue:
            row, col, count = queue.popleft()

            if (row == (rows - 1) or row == 0 or col == (columns - 1) or col == 0) and [
                row,
                col,
            ] != entrance:
                return count

            for d_row, d_col in directions:
                next_row, next_col = row + d_row, col + d_col

                if (
                    next_row >= 0
                    and next_row < rows
                    and next_col >= 0
                    and next_col < columns
                    and maze[next_row][next_col] == "."
                ):
                    queue.append((next_row, next_col, count + 1))
                    maze[next_row][next_col] = "+"

        return -1
