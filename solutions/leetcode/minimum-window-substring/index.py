from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        target, window = defaultdict(int), defaultdict(int)
        for c in t:
            target[c] += 1

        have, need = 0, len(target)
        result, result_length = [-1, -1], float("inf")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            if c in target and window[c] == target[c]:
                have += 1

            while have == need:
                if (right - left + 1) < result_length:
                    result = [left, right]
                    result_length = right - left + 1

                window[s[left]] -= 1
                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1
                left += 1

        left, right = result
        return s[left: right + 1] if result_length != float("inf") else ""
