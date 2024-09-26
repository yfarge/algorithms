from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        low, high = 0, m - 1

        while low <= high:
            mid = (low + high) // 2
            col = mat[mid].index(max(mat[mid]))

            bottom = mat[mid + 1][col] if mid + 1 < m else -1
            top = mat[mid - 1][col] if mid - 1 >= 0 else -1

            if bottom < mat[mid][col] > top:
                return [mid, col]
            elif mat[mid][col] > bottom:
                high = mid - 1
            else:
                low = mid + 1

        return [mid, col]

