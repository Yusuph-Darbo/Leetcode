# Approach:
# Use a stack to process the characters in the string.
#
# Iterate through each character in the string:
# - If the stack is not empty and the top of the stack is equal to the current character,
#   pop the top element from the stack to remove the duplicate pair.
#
# - Otherwise, push the current character onto the stack.
#
# This ensures that whenever two adjacent duplicate characters are found,
# they are removed immediately.
#
# After processing all characters, the stack contains the final string with no adjacent duplicates.
#
# Join the stack into a string and return the result.
#
# Time Complexity: O(n) 
# Space Complexity: O(n) 


class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []


        for char in s:
            # Returns the top value of the stack
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)