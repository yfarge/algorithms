from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 0
        digits[-1] += 1
        for digit in reversed(digits):
            total = digit + carry
            carry = total // 10
            result.append(total % 10)

        if carry:
            result.append(carry)

        result.reverse()
        return result
