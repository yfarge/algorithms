from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1

        while low <= high:
            mid = low + (high - low) // 2
            row, col = mid // n, mid % n

            if matrix[row][col] < target:
                low = mid + 1
            elif matrix[row][col] > target:
                high = mid - 1
            else:
                return True

        return False
