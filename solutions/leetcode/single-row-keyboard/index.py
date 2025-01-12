class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = {c: i for i, c in enumerate(keyboard)}
        res = i = 0
        for c in word:
            j = pos[c]
            res += abs(i - j)
            i = j
        return res
