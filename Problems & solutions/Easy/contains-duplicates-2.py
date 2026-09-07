# Approach:
# Use a sliding window with a set to track the last k elements.
#
# Iterate through the array:
# - If the current number is already in the set, it means the same value
#   exists within distance k, so return True.
#
# - Otherwise, add the current number to the set.
#
# - If the size of the set exceeds k, remove the element that is now
#   outside the sliding window (nums[i - k]).
#
# This ensures the set always contains at most k recent elements.
#
# If no duplicates are found within distance k, return False.
#
# Time Complexity: O(n) — each element is added and removed at most once.
# Space Complexity: O(k) — the set stores at most k elements.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        table = set()

        for i in range(len(nums)):
            if nums[i] in table:
                return True

            table.add(nums[i])

            if len(table) > k:
                table.remove(nums[i - k])

        return False