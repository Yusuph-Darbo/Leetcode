# Approach:
# Traverse the array and count consecutive zeros.
# For each zero, add the current streak length to the result,
# which accounts for all subarrays ending at that index.
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
