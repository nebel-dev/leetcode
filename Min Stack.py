import math


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [math.inf]a

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x <= self.min_stack[-1]:
            self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


obj = MinStack()
obj.push(-3)
obj.push(0)
obj.push(1)
obj.push(-4)
print(obj)
print("top:", obj.top())
print("min:", obj.getMin())
obj.pop()
print("top:", obj.top())
print("min:", obj.getMin())
