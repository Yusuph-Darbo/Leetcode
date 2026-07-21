# Approach:
# Maintain two stacks: one for all values and another for the minimum value
# at each position. This allows push, pop, top, and getMin operations to be
# performed in constant time.
#
# Time: O(1) per operation
# Space: O(n)


class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.minStack:
            value = min(value, self.minStack[-1])
        self.minStack.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
