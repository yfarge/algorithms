class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = max_frequency = result = 0
        count = {}
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_frequency = max(max_frequency, count[s[right]])

            if (right - left + 1) - max_frequency <= k:
                result = max(result, right - left + 1)
            else:
                count[s[left]] -= 1
                left += 1

        return result
