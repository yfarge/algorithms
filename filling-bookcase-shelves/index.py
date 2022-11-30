from typing import *


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        n = len(books)
        memo = {}

        def dp(i, current_height, remaining_width):
            if (i, current_height, remaining_width) in memo:
                return memo[(i, current_height, remaining_width)]

            if i == n:
                return current_height

            width, height = books[i]

            # add book on new shelf
            res = dp(i + 1, height, shelfWidth - width) + current_height

            # add on current level
            if (width <= remaining_width):
                res = min(res, dp(i+1, max(current_height, height),
                          remaining_width - width))

            memo[(i, current_height, remaining_width)] = res
            return res

        return dp(0, 0, shelfWidth)
