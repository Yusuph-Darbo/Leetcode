# Approach:
# Use two pointers to check if string s is a subsequence of string t.
# Pointer i tracks position in s, and pointer j scans through t.
# Each time a matching character is found, move pointer i forward.
# If pointer i reaches the end of s, all characters were found in order.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        i = 0

        for j in range(len(t)):

            if i == len(s):
                return True

            if s[i] == t[j]:
                i += 1

        return i == len(s)
