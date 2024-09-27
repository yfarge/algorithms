from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row: int, col: int, i: int):
            if i == len(word):
                return True

            if not (0 <= row < m and 0 <= col < n and board[row][col] == word[i]):
                return False

            board[row][col] = "#"
            for next_row, next_col in [
                (row - 1, col),
                (row, col + 1),
                (row + 1, col),
                (row, col - 1),
            ]:
                if backtrack(next_row, next_col, i + 1):
                    return True

            board[row][col] = word[i]
            return False

        m, n = len(board), len(board[0])
        for row in range(m):
            for col in range(n):
                if backtrack(row, col, 0):
                    return True

        return False

