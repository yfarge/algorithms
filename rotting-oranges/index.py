from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_count = minute = 0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        while queue and fresh_count > 0:
            minute += 1

            for _ in range(len(queue)):
                current_row, current_col = queue.popleft()

                for next_row, next_col in [
                    (current_row, current_col - 1),
                    (current_row - 1, current_col),
                    (current_row, current_col + 1),
                    (current_row + 1, current_col),
                ]:
                    if (
                        rows > next_row >= 0
                        and cols > next_col >= 0
                        and grid[next_row][next_col] == 1
                    ):
                        grid[next_row][next_col] = 2
                        fresh_count -= 1
                        queue.append((next_row, next_col))

        return minute if fresh_count == 0 else -1
