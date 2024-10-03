from typing import List
from collections import Counter
from heapq import heapify, heappop


# O(nlog(k))
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = [(-count, value) for value, count in counter.items()]
        heapify(heap)

        result = []
        for _ in range(k):
            _, value = heappop(heap)
            result.append(value)
        return result


# O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [list() for _ in range(len(nums))]
        for value, count in counter.items():
            buckets[count - 1].append(value)

        result = []
        for i in range(len(nums) - 1, -1, -1):
            for value in buckets[i]:
                result.append(value)
            if len(result) == k:
                return result

        return result
