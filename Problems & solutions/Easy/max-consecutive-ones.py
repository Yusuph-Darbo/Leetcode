# Approach:
# Track the current streak of consecutive 1s and update the maximum streak
# whenever a 1 is encountered. Reset the current streak when a 0 appears.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = 0
        rev = 0

        for i in nums:
            if i == 1:
                cur += 1
                if cur > rev:
                    rev = cur
            else:
                cur = 0

        return rev
