class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        vowels = ["a", "e", "i", "o", "u"]

        def isVowel(i):
            return chars[i].lower() in vowels

        start, end = 0, len(s) - 1

        while start < end:
            while not isVowel(start) and start < end:
                start += 1
            while not isVowel(end) and end > 0:
                end -= 1

            if isVowel(start) and isVowel(end):
                chars[start], chars[end] = chars[end], chars[start]
                start += 1
                end -= 1

        return "".join(chars)
