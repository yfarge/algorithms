from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            row = [None for _ in range(i + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, i):
                row[j] = result[-1][j - 1] + result[-1][j]

            result.append(row)

        return result
