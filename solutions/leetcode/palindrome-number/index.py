class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_x, y = 0, x
        while y > 0:
            reversed_x *= 10
            reversed_x += y % 10
            y = y // 10
        return reversed_x == x
