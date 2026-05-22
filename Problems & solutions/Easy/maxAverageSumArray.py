# Approach:
#
# Use a sliding window of size k to track the sum of consecutive elements.
# First, calculate the sum of the first window of size k.
# Then slide the window forward one element at a time by:
#
# - subtracting the element leaving the window
# - adding the element entering the window
#
# Keep track of the maximum sum seen.
# Finally, divide the maximum sum by k to get the maximum average.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Returns a new sub array not inclusive
        curr = sum(nums[:k])
        total = curr

        for i in range(k, len(nums)):
            
            # Remove last element and add next element
            curr = curr - nums[i - k] + nums[i]
            total = max(total, curr)


        return total / float(k)