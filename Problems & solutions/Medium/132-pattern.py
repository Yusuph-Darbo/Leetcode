# Approach:
# Use a stack to track potential 3-2 pairs and maintain the minimum value
# seen so far as the 1. Check whether the current number forms a 1-3-2 pattern.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []
        cur_minimum = nums[0]

        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()

            if stack and n > stack[-1][1]:
                return True

            stack.append([n, cur_minimum])
            cur_minimum = min(n, cur_minimum)

        return False
