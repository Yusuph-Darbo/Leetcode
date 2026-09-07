# Approach:
# Use two pointers to keep at most two occurrences of each number. If the
# current number is greater than the element two positions behind, keep it.
#
# Time: O(n)
# Space: O(1)


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i
