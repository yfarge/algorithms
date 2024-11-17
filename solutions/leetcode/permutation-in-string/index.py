class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        current, target = [0] * 26, [0] * 26
        for i in range(len(s1)):
            target[ord(s1[i]) - ord('a')] += 1
            current[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += 1 if current[i] == target[i] else 0

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[right]) - ord('a')
            current[index] += 1
            if current[index] == target[index]:
                matches += 1
            elif current[index] == target[index] + 1:
                matches -= 1

            index = ord(s2[left]) - ord('a')
            current[index] -= 1
            if current[index] == target[index]:
                matches += 1
            elif current[index] == target[index] - 1:
                matches -= 1

            left += 1

        return matches == 26
