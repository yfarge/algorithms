from typing import List
from operator import itemgetter


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeed = sorted(zip(position, speed), key=itemgetter(0))
        stack = []
        for i in range(len(positionSpeed)):
            position, speed = positionSpeed[i]
            step = (target - position) / speed
            while stack and stack[-1] <= step:
                stack.pop()
            stack.append(step)
        return len(stack)
