from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pairs = zip_longest(word1, word2, fillvalue="")
        return "".join([char for pair in pairs for char in pair])

