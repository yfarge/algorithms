from typing import List
import sys


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n1, n2 = sys.maxsize, sys.maxsize

        for num in nums:
            if num <= n1:
                n1 = num
            elif num <= n2:
                n2 = num
            else:
                return True

        return False

