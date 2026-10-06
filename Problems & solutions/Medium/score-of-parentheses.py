# Approach:
# Use a stack to store the score of each nested level. When ')' is found,
# calculate the current group's score and add it to its parent level.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for char in s:
            if char == "(":
                stack.append(0)
            else:
                v = stack.pop()
                w = stack.pop()
                stack.append(w + max(2 * v, 1))

        return stack.pop()
