from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(row: int, col: int, wordIndex: int):
            if wordIndex == len(word):
                return True

            if (
                row < 0
                or m <= row
                or col < 0
                or n <= col
                or board[row][col] != word[wordIndex]
            ):
                return False

            board[row][col] = "#"

            result = (
                backtrack(row, col - 1, wordIndex + 1)
                or backtrack(row - 1, col, wordIndex + 1)
                or backtrack(row, col + 1, wordIndex + 1)
                or backtrack(row + 1, col, wordIndex + 1)
            )

            board[row][col] = word[wordIndex]

            return result

        return any(backtrack(i, j, 0) for i in range(m) for j in range(n))
