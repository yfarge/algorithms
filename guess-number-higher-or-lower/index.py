# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            answer = left + (right - left) // 2
            direction = guess(answer)
            if direction == 0:
                return answer
            if direction < 0:
                right = answer - 1
            else:
                left = answer + 1
        return 0
