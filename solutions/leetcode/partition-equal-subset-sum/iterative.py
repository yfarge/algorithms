from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        dp = set()
        dp.add(0)

        target = total // 2
        for num in nums:
            nextDp = set()
            for subset_sum in dp:
                nextDp.add(num + subset_sum)
                nextDp.add(subset_sum)
                if target in dp:
                    return True
            dp = nextDp

        return False
