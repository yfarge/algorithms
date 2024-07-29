from typing import List


class Solution:
    def numHours(self, piles: List[int], k: int):
        hours = 0
        for count in piles:
            hours += -(count // -k)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low <= high:
            mid = (low + high) // 2

            if self.numHours(piles, mid) > h:
                low = mid + 1
            else:
                high = mid - 1

        return low
