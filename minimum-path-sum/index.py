from typing import *


# def minPathSum(grid: List[List[int]]) -> int:
#     m = len(grid[0])
#     n = len(grid)
#     dp = [[0 for _ in range(m)] for _ in range(n)]

#     def checkPaths(position: Tuple[int, int], agg: int) -> int:
#         i, j = position
#         if i >= m or j >= n:
#             return agg

#         agg += grid[j][i]
#         if position == (m - 1, n - 1):
#             return agg


#         dp[j][i] = min(
#             dp[j][i] +checkPaths((i + 1, j), agg),
#             checkPaths((i, j + 1), agg),
#         )

#     checkPaths((0, 0), 0)
#     print(dp)
#     return dp[m - 1][n - 1]

def minPathSum(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])

    res = [[float('inf') for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
    res[ROWS - 1][COLS] = 0

    for r in range(ROWS - 1, -1, -1):
        for c in range(COLS - 1, -1, -1):
            res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])

    return res[0][0]


grid = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]


print(minPathSum(grid))
# print("m", len(grid[0]))
# print("n", len(grid))
