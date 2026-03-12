class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Make a dict
        # Iterate through the arr
        # Store each number in the dict and its frequency

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
        