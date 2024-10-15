class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(needle), len(haystack) + 1):
            if haystack[i - len(needle): i] == needle:
                return i - len(needle)
        return -1
