from typing import List
from bisect import bisect_left


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        m = len(potions)
        max_potion = potions[m - 1]
        answer = []
        for spell in spells:
            min_potion = -(success // -spell)
            if min_potion > max_potion:
                answer.append(0)
                continue
            index = bisect_left(potions, min_potion)
            answer.append(m - index)

        return answer


# Custom Bisect Left
class Solution:
    def bisectLeft(self, arr: List[int], target: int) -> int:
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low

    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        m = len(potions)
        max_potion = potions[m - 1]
        answer = []
        for spell in spells:
            min_potion = -(success // -spell)
            if min_potion > max_potion:
                answer.append(0)
                continue
            index = self.bisectLeft(potions, min_potion)
            answer.append(m - index)

        return answer
