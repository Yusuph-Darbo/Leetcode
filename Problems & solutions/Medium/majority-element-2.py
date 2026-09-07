# Approach:
# Use the Boyer-Moore Voting Algorithm (extended for n/3 case) to find up to
# two potential majority candidates, then verify their counts in a second pass.
#
# Time: O(n)
# Space: O(1)


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        arr = []
        candiate1 = 0
        candiate2 = 1
        count1 = 0
        count2 = 0

        for num in nums:
            if candiate1 == num:
                count1 += 1

            elif candiate2 == num:
                count2 += 1

            elif count1 == 0:
                candiate1 = num
                count1 = 1

            elif count2 == 0:
                candiate2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        for num in (candiate1, candiate2):
            if nums.count(num) > len(nums) // 3:
                arr.append(num)

        return arr
