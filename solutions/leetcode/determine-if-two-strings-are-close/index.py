from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # length check
        if len(word1) != len(word2):
            return False

        # unique characters check
        if set(word1) != set(word2):
            return False

        # build frequency maps
        frequencies_one = Counter(word1)
        frequencies_two = Counter(word2)

        occurences_one = sorted(frequencies_one.values())
        occurences_two = sorted(frequencies_two.values())

        # occurences check
        return occurences_one == occurences_two
