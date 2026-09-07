# Approach:
# Use the XOR (^) bitwise operator to find the element that appears only once.
# By XORing all numbers in the array, all duplicate numbers cancel out,
# leaving only the number that appears once.
#
# Time Complexity: O(n)
# Space Complexity: O(1) 

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        for num in nums:
            res ^= num

        return res