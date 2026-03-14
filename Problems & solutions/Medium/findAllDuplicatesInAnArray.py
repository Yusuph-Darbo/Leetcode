# Approach:
# Use a hash table to count the frequency of each number in the array.
# After counting, collect the numbers that appear exactly twice.
#
# Time: O(n)
# Space: O(n)

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        arr = []

        table = {}

        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1

        for key, value in table.items():
            if value == 2:
                arr.append(key)

        return arr
        