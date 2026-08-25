# Approach:
# Traverse from right to left, adding one to the first digit that is not 9.
# Set trailing 9s to 0, and add a leading 1 if all digits were 9.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits

            digits[i] = 0

            if i == 0:
                return [1] + digits
