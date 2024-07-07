from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            stack.append(asteroid)

            while len(stack) > 1 and stack[-1] < 0 and stack[-2] > 0:
                if abs(stack[-2]) < abs(asteroid):
                    stack.pop()
                    stack.pop()
                    stack.append(asteroid)
                elif abs(asteroid) < abs(stack[-2]):
                    stack.pop()
                else:
                    stack.pop()
                    stack.pop()

        return stack
