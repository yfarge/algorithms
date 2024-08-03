class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n

        if n == 3:
            return 5

        MOD = 1_000_000_007
        n1, n2, n3 = 5, 2, 1
        for i in range(4, n + 1):
            temp = 2 * n1 + n3
            n2, n3 = n1, n2
            n1 = temp % MOD

        return n1
