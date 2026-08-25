# Approach:
# Track the current streak of consecutive zeros. Each new zero creates
# count new zero-filled subarrays ending at that position.
#
# Time: O(n)
# Space: O(1)


class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res, count = 0, 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count = 0
            res += count

        return res
