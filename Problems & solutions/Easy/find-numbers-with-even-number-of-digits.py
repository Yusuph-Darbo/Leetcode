# Approach:
# Convert each number to a string and check if it contains an even number
# of digits. Increment the count for each matching number.
#
# Time: O(n * m)
# Space: O(m)


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for i in nums:

            i = str(i)

            if len(i) % 2 == 0:
                count += 1

        return count
