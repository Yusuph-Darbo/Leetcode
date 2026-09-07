# Approach:
# Use a stack to evaluate the expression from left to right. Push operands
# onto the stack, and whenever an operator is encountered, pop the required
# operands, apply the operation, and push the result back onto the stack.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                second, first = stack.pop(), stack.pop()
                # Python rounding rounds to negative inf, instead of 0
                stack.append(int(first / second))
            else:
                stack.append(int(t))

        return stack[0]
