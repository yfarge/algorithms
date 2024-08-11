from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_map = Counter(magazine)

        for char in ransomNote:
            if not magazine_map[char]:
                return False
            magazine_map[char] -= 1

        return True
