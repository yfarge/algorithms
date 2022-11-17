class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        # if the string is empty, return 0
        if n == 0:
            return 0

        value = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
                 "L": 50,  "C": 100,  "D": 500, "M": 1000}

        result = value[s[-1]]
        for i in reversed(range(n - 1)):
            if (value[s[i]] < value[s[i+1]]):
                result -= value[s[i]]
            else:
                result += value[s[i]]
        return result
