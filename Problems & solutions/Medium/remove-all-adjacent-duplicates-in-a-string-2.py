# Approach:
# Use a stack to track each character and its consecutive count. When a count
# reaches k, remove that group, allowing adjacent groups to merge naturally.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])

        res = "".join(c * count for c, count in stack)

        return res
