from typing import List
from collections import deque


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        queue = deque([(sr, sc)])
        starting_color = image[sr][sc]
        m, n = len(image), len(image[0])

        while queue:
            current_row, current_col = queue.popleft()
            image[current_row][current_col] = color

            for d_row, d_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                next_row, next_col = current_row + d_row, current_col + d_col

                if (
                    0 <= next_row < m
                    and 0 <= next_col < n
                    and image[next_row][next_col] == starting_color
                ):
                    queue.append((next_row, next_col))

        return image
