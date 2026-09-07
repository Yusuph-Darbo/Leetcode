# Approach:
# Store the input array and compute the sum of elements between
# indices left and right (inclusive) by iterating through the range.
#
# Time: O(n) per query
# Space: O(1)


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        value = 0
        for i in range(left, right + 1):
            value += self.nums[i]

        return value


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
