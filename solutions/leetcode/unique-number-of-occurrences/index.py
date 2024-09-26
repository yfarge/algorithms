from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequencies = {}
        for num in arr:
            frequencies[num] = frequencies.setdefault(num, 0) + 1

        occurences = set()
        for frequency in sorted(frequencies.values()):
            if frequency in occurences:
                return False
            occurences.add(frequency)

        return True
