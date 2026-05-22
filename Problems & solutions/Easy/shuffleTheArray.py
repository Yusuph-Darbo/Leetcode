# Approach:
# Use two pointers to split the array into two halves.
# Iterate through both halves simultaneously and append elements alternately.
# Continue until all elements from both halves are added to the result.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        arr = []

        ptr1 = 0
        ptr2 = n

        while ptr1 < n and ptr2 < len(nums):

            arr.append(nums[ptr1])
            arr.append(nums[ptr2])

            ptr1 += 1
            ptr2 += 1

        return arr
