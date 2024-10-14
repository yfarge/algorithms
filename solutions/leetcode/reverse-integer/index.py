class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        abs_x = abs(x)
        lb, rb = -pow(2, 31), pow(2, 31) - 1

        while abs_x:
            result = result * 10 + abs_x % 10
            abs_x = abs_x // 10
            if not (lb <= result <= rb):
                return 0

        return result if x > 0 else -result
