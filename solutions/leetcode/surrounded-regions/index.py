from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m, n = len(board), len(board[0])
        stack = []
        for i in range(m):
            if board[i][0] == "O":
                stack.append((i, 0))
            if board[i][n - 1] == "O":
                stack.append((i, n - 1))

        for j in range(n):
            if board[0][j] == "O":
                stack.append((0, j))
            if board[m - 1][j] == "O":
                stack.append((m - 1, j))

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
                    and board[next_row][next_col] == "O"
                ):
                    stack.append((next_row, next_col))

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    board[i][j] = "X"
