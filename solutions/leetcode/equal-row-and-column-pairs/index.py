from typing import List
from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        seen_rows = Counter(map(tuple, grid))
        transposed_grid = zip(*grid)

        count = 0
        for col in transposed_grid:
            if col in seen_rows:
                count += seen_rows[col]

        return count
