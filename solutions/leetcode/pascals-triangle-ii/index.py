from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex + 1):
            row = [None for _ in range(i + 1)]
            row[0] = row[-1] = 1

            for j in range(1, i):
                row[j] = result[j - 1] + result[j]
            result = row

        return result
