class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}

        curr_count = 0
        for i in range(k):
            if s[i] in vowels:
                curr_count += 1

        max_count = curr_count
        for i in range(len(s) - k):
            if s[i] in vowels:
                curr_count = max(curr_count - 1, 0)
            if s[i + k] in vowels:
                curr_count += 1
            if curr_count > max_count:
                max_count = curr_count
        return max_count

