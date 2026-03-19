# Approach:
# Use prefix and postfix products to compute the result without division.
# First pass stores the product of all elements to the left of each index,
# second pass multiplies by the product of elements to the right.
#
# Time: O(n)
# Space: O(1) extra (output array not counted)


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        arr = [1] * n

        prefix = 1

        for i in range(n):
            arr[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            arr[i] *= postfix
            postfix *= nums[i]

        return arr
