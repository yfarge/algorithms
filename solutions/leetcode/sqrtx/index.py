class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = low + (high - low) // 2
            total = mid * mid

            if total < x:
                low = mid + 1
            elif total > x:
                high = mid - 1
            else:
                return mid

        return high
