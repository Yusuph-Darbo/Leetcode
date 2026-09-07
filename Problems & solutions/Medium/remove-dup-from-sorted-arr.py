# Approach:
# Use a two-pointer technique to modify the sorted array in-place.
# Maintain a write pointer `i` that tracks the position where the next
# valid element should be placed.
#
# The first two elements are always allowed (since each number can appear at most twice).
# For the remaining elements, only place the current number `n` if:
# - We have written fewer than 2 elements so far, OR
# - The current number is greater than nums[i-2].
#
# Because the array is sorted, if nums[i-2] equals n, it means we have
# already kept two copies of that number, so we skip it.
#
#
# Time Complexity: O(n) — we traverse the array once.
# Space Complexity: O(1) — modification is done in-place using a single pointer.


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i

       