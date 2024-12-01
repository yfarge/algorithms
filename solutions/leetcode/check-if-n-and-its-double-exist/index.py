from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for num in arr:
            t1 = 2 * num
            t2 = num / 2
            if t1 in s or t2 in s:
                return True
            s.add(num)
        return False
