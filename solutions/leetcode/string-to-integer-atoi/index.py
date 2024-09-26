class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1

        if i >= len(s):
            return 0

        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1

        while i < len(s) and s[i] == "0":
            i += 1

        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        return min(max(sign * num, -pow(2, 31)), pow(2, 31) - 1)
