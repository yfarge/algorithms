from typing import List
from collections import defaultdict


# using sorted string as key
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            group = "".join(sorted(s))
            groups[group].append(s)
        return groups.values()


# using frequency as key
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            groups[tuple(count)].append(s)
        return groups.values()
