class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromCenter(left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1: right]

        longest_palindrome = ""
        for index in range(len(s)):
            longest_palindrome = max(
                longest_palindrome,
                expandFromCenter(index, index),
                expandFromCenter(index, index + 1),
                key=len,
            )

        return longest_palindrome
