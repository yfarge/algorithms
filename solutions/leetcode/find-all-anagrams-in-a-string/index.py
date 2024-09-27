from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        current, goal = Counter(), Counter(p)

        left = 0
        for right in range(len(s)):
            current[s[right]] += 1
            if right >= len(p):
                current[s[left]] -= 1
                left += 1

            if current == goal:
                answer.append(left)

        return answer
