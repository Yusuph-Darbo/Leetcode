# Approach:
# Use a stack to handle operator precedence. Parse multi-digit numbers,
# apply addition and subtraction by pushing signed values, and evaluate
# multiplication and division immediately using the stack's top element.
# Sum the stack at the end to obtain the result.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def calculate(self, s: str) -> int:
        op, val = "+", 0
        stack = []

        for i, x in enumerate(s):
            if x.isdigit():
                val = 10 * val + int(x)

            if x in "+-*/" or i == len(s) - 1:
                if op == "+":
                    stack.append(val)
                elif op == "-":
                    stack.append(-val)
                elif op == "*":
                    stack.append(stack.pop() * val)
                else:
                    stack.append(int(stack.pop() / val))

                op, val = x, 0

        return sum(stack)
