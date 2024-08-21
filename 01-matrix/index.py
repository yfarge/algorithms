from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float("inf")

        while queue:
            row, col = queue.popleft()

            for next_row, next_col in [
                (row - 1, col),
                (row, col + 1),
                (row + 1, col),
                (row, col - 1),
            ]:
                if (
                    0 <= next_row < m
                    and 0 <= next_col < n
                    and mat[next_row][next_col] > mat[row][col] + 1
                ):
                    queue.append((next_row, next_col))
                    mat[next_row][next_col] = mat[row][col] + 1

        return mat
