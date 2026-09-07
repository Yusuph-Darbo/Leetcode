# Approach:
# Iterate through each character in the string.
#
# Check if the character is alphanumeric using isalnum().
# If it is, convert it to lowercase and store it in a new list.
#
# This removes spaces, punctuation, and makes the comparison case-insensitive.
#
# After building the cleaned list, compare it with its reverse.
#
# If both are the same, the string is a palindrome.
# Otherwise, it is not.
#
# Time Complexity: O(n) — we iterate through the string once.
# Space Complexity: O(n) — we store the cleaned characters in a list.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newWord = []
        for char in s:
            if char.isalnum():
                newWord.append(char.lower())

        return newWord == newWord[::-1]

        