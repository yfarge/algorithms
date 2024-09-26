from typing import List
from heapq import heappush, heappop
from operator import itemgetter


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res, prefixSum, minHeap = 0, 0, []
        pairs = sorted(list(zip(nums1, nums2)),
                       key=itemgetter(1), reverse=True)

        for n1, n2 in pairs:
            prefixSum += n1
            heappush(minHeap, n1)
            if len(minHeap) == k:
                res = max(res, prefixSum * n2)
                prefixSum -= heappop(minHeap)
        return res
