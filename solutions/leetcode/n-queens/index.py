from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, board = [], [["."] * n for _ in range(n)]
        cols, posDiag, negDiag = set(), set(), set()

        def backtrack(i: int):
            if i >= n:
                res.append(["".join(row) for row in board])
                return

            for j in range(n):
                if j in cols or i - j in negDiag or i + j in posDiag:
                    continue
                board[i][j] = 'Q'
                cols.add(j)
                negDiag.add(i - j)
                posDiag.add(i + j)
                backtrack(i + 1)
                board[i][j] = '.'
                cols.discard(j)
                negDiag.discard(i - j)
                posDiag.discard(i + j)

        backtrack(0)
        return res
