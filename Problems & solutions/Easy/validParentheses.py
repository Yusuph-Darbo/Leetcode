# Approach:
# Use a stack to keep track of opening brackets.
#
# Create a dictionary that maps each closing bracket to its corresponding opening bracket.
#
# Iterate through each character in the string:
# - If the character is a closing bracket, check if the stack is empty
#   or if the top of the stack is not the matching opening bracket.
#   If either is true, return False.
#
# - If the character is an opening bracket, push it onto the stack.
#
# After processing all characters, check if the stack is empty.
# If it is empty, all brackets were matched correctly.
# Otherwise, return False.
#
# Time Complexity: O(n)
# Space Complexity: O(n) 


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        mapping = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for char in s:
            if char in mapping:

                # Checking if the stack is empty or the popped value != 
                if not stack or stack.pop() != mapping[char]:
                    return False
            
            else:
                stack.append(char)

        return len(stack) == 0
