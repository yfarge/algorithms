class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a | b != c:
            if (a & 1 | b & 1) != c & 1:
                count += (a & 1 & b & 1) + 1

            a >>= 1
            b >>= 1
            c >>= 1

        return count
