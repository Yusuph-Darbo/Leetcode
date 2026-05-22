# Approach:
# Use a temporary array and place each element at its rotated index
# using (i + k) % n, then copy the result back into nums.
#
# Time: O(n)
# Space: O(n)

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Use the modulo operator 
        
        n = len(nums)
        newArr = [0] * n

        for i in range(n):
            newArr[(i + k) % n] = nums[i]

        for i in range(n):
            nums[i] = newArr[i]