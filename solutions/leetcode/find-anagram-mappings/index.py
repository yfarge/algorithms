from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = {v: i for i, v in enumerate(nums2)}
        return [lookup[v] for v in nums1]
