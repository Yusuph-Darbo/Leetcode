# Approach:
# Use two pointers starting from the end of both strings.
#
# Maintain a variable `carry` to store overflow from digit addition.
#
# While either pointer is valid or carry exists:
#   - Convert the current character to its integer value
#     using ord(char) - ord('0').
#   - Add both digits and the carry.
#   - Update the carry (total // 10).
#   - Append the current digit (total % 10) to a result list.
#
# After processing all digits, reverse the result list
# since digits were added from least significant to most significant.
#
# Return the joined string.
#
# Time Complexity: O(n)
# Space Complexity: O(n) 

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0
        total = []

        while i >= 0 or j >= 0 or carry:
            val1 = 0
            val2 = 0
            if i >= 0:
                val1 = ord(num1[i]) - ord('0')

            if j >= 0:
                val2 = ord(num2[j]) - ord('0')

            totalVal = val1 + val2 + carry
            carry = totalVal // 10

            total.append(str(totalVal % 10))

            i -= 1
            j -= 1

        return ''.join(reversed(total))