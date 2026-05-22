# Approach:
# Convert nums into a set for O(1) lookups.
# Start sequences only from numbers that have no left neighbor (num - 1 not in set).
# For each start, expand forward while consecutive numbers exist.
# Track the longest sequence length found.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        length = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                next_val = num + 1

                while next_val in set_nums:
                    next_val += 1

                length = max(next_val - num, length)

        return length
