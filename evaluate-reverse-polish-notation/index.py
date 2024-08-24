from typing import List
import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b),
        }

        stack = []
        for token in tokens:
            if token not in operations.keys():
                stack.append(int(token))
                continue

            right, left = stack.pop(), stack.pop()
            stack.append(operations[token](left, right))

        return stack[0]
