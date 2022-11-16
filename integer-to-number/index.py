class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        bases = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        romans = ["I", "IV", "V", "IX", "X", "XL",
                  "L", "XC", "C", "CD", "D", "CM", "M"]
        res = ""
        temp = num
        for i in reversed(range(13)):
            base, roman = bases[i], romans[i]
            count = temp // base
            res += count * roman
            temp -= count * base
        return res
