class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(end: int):
            if len1 % end or len2 % end:
                return False
            f1, f2 = len1 // end, len2 // end
            return str1[:end] * f1 == str1 and str1[:end] * f2 == str2

        for end in range(min(len1, len2), 0, -1):
            if isDivisor(end):
                return str1[:end]
        return ""
