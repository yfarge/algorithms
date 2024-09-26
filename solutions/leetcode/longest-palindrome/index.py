from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = offset = 0
        for count in Counter(s).values():
            if count % 2 == 0:
                result += count
            else:
                result += count - 1
                offset = 1

        return result + offset
