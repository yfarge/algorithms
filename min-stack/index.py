class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minimums.append(val)
        else:
            self.stack.append(val)
            self.minimums.append(min(val, self.minimums[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minimums.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
