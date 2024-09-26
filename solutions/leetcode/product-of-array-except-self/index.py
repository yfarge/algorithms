from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length
        answer[0] = 1

        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]

        suffix = 1

        for i in reversed(range(length - 1)):
            suffix *= nums[i + 1]
            answer[i] = suffix * answer[i]

        return answer
