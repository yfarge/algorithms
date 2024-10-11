from typing import List
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        n = len(arr)
        counter = Counter(arr)
        buckets = [0] * (n + 1)

        for count in counter.values():
            buckets[count] += 1

        result = len(counter)
        for i in range(1, n + 1):
            if k < i:
                return result

            removed_elements = min(k // i, buckets[i])
            k -= (i * removed_elements)
            result -= removed_elements

        return result
