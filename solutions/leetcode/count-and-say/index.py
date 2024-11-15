class Solution:
    def rleEncode(self, s: str):
        if not s:
            return ""

        result = ""
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result += str(count) + s[i - 1]
                count = 1

        result += str(count) + s[-1]

        return result

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        return self.rleEncode(self.countAndSay(n - 1))
