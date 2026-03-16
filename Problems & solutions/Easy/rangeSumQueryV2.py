# Approach:
# Build a prefix sum array where prefix[i] stores the sum of the first i elements.
# The sum of any range [left, right] can then be computed in O(1) using
# prefix[right + 1] - prefix[left].
#
# Time: O(n) to build, O(1) per query
# Space: O(n)


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
