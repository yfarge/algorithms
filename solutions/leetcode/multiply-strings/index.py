class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0

        for char in num1:
            n1 *= 10
            n1 += ord(char) - ord('0')

        for char in num2:
            n2 *= 10
            n2 += ord(char) - ord('0')

        return str(n1 * n2)
