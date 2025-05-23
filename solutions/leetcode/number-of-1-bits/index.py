class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            result += n & 1
            n >>= 1
        return result
