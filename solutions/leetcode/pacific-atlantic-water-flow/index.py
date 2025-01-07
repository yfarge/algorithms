from typing import List, Tuple


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def dfs(stack: List[Tuple[int, int]]):
            visited = set(stack)

            while stack:
                row, col = stack.pop()
                visited.add((row, col))

                for next_row, next_col in [
                    (row, col - 1),
                    (row - 1, col),
                    (row, col + 1),
                    (row + 1, col),
                ]:
                    if (
                        0 <= next_row < m
                        and 0 <= next_col < n
                        and (next_row, next_col) not in visited
                        and heights[next_row][next_col] >= heights[row][col]
                    ):
                        stack.append((next_row, next_col))

            return visited

        pacific = dfs(
            [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
        )

        atlantic = dfs(
            [(m - 1, j) for j in range(n)] + [(i, n - 1) for i in range(m)]
        )

        return list(pacific & atlantic)
