# Two-pointer approach:
        # i = tracks the position of the next unique element
        # j = scans through the array
        # Whenever nums[j] is different from the last unique element (nums[i-1]),
        # place nums[j] at nums[i] and move i forward.
        #
        # Since the array is sorted, duplicates will be adjacent.
        # At the end, i will represent the count of unique elements.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        return i # The number of unique elements
