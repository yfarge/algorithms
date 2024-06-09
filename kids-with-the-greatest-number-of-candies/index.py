from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [max(candies) <= (count + extraCandies) for count in candies]
