class MinStack:

    def __init__(self):
        self.stack = []
        self.tempStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.tempStack:
            minimum = min(self.tempStack[-1], val)
        else:
            minimum = val
        self.tempStack.append(minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.tempStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.tempStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()