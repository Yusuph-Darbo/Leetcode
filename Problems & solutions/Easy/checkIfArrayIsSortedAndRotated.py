# Approach:
# Count the number of places where the array decreases.
# A sorted and rotated array can have at most one drop
# where the previous element is greater than the current one.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def check(self, nums: List[int]) -> bool:
        valid = False
        for i in range(len(nums)):
            if nums[i - 1] > nums[i]:
                if valid:
                    return False
                valid = True

        return True
