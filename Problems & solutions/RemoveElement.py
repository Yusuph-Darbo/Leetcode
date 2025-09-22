# Two-pointer approach:
        # j = tracks position of the next valid element
        # i = scans through the array
        # When nums[i] is not equal to val, copy it to nums[j] and move j forward.
        # Elements equal to val are skipped/overwritten.
        #
        # At the end, j represents the new length of the array without val.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j +=1 

        return j
