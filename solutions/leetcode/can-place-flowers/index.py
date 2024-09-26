from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def isValidPlot(p):
            l_value = flowerbed[p - 1] if p > 0 else 0
            c_value = flowerbed[p]
            r_value = flowerbed[p + 1] if p < len(flowerbed) - 1 else 0

            return c_value == 0 and l_value == 0 and r_value == 0

        for p in range(len(flowerbed)):
            if n == 0:
                return True

            if isValidPlot(p):
                flowerbed[p] = 1
                n -= 1

        return n == 0
