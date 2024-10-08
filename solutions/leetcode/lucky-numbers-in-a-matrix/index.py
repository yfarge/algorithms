from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        min_row = [float('inf')] * m
        max_col = [0] * n

        for row in range(m):
            for col in range(n):
                min_row[row] = min(min_row[row], matrix[row][col])
                max_col[col] = max(max_col[col], matrix[row][col])

        result = []
        for row in range(m):
            for col in range(n):
                if min_row[row] == max_col[col]:
                    result.append(matrix[row][col])

        return result
