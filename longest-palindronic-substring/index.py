class Solution(object):
    """
    :type s: str
    :rtype: str
    """

    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            odd_palindrone = self.expandFromCenter(i, i, s)
            even_palindrone = self.expandFromCenter(i, i + 1, s)
            if (len(odd_palindrone) > len(res)):
                res = odd_palindrone
            if (len(even_palindrone) > len(res)):
                res = even_palindrone
        return res

    def expandFromCenter(self, l, r, s):
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return s[l + 1: r]
