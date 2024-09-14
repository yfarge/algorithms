from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row: int, col: int):
            nonlocal m, n
            stack = [(row, col)]
            while stack:
                row, col = stack.pop()

                if grid[row][col] != "1":
                    continue

                grid[row][col] = "2"

                for next_row, next_col in [
                    (row - 1, col),
                    (row, col + 1),
                    (row + 1, col),
                    (row, col - 1),
                ]:
                    if (
                        0 <= next_row < m
                        and 0 <= next_col < n
                        and grid[next_row][next_col] == "1"
                    ):
                        stack.append((next_row, next_col))

        answer = 0
        m, n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    answer += 1
                    dfs(row, col)

        return answer
