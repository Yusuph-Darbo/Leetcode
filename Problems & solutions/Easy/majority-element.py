# Approach:
# Use a hash map (Counter) to count the frequency of each number.
# Then iterate through the map to find the number with the highest frequency.
# The majority element is guaranteed to exist and appears more than ⌊n/2⌋ times.
# 
# Why this works:
# The majority element will always have the maximum count in the frequency table.
# 
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = Counter(nums)

        maxCount = 0
        result = 0

        for key, value in table.items(): 
            
            if value > maxCount:
                maxCount = value
                result = key

        return result
        