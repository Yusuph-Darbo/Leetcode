# Approach:
# Use two dictionaries to track character mappings between s and t.
#
# Iterate through both strings at the same time.
#
# Check if the current characters have been mapped before.
# If the mapping is inconsistent, return False.
#
# Otherwise, store the mapping in both dictionaries.
#
# If all mappings are consistent, return True.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        string1 = {}
        string2 = {}

        for i in range(len(s)):

            if s[i] in string1 and string1[s[i]] != t[i]:
                return False
            if t[i] in string2 and string2[t[i]] != s[i]:
                return False

            string1[s[i]] = t[i]
            string2[t[i]] = s[i]

        return True     