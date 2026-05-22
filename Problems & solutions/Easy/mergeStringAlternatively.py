# Approach:
# Use two pointers to iterate through both strings.
# Append characters alternately from each string while either pointer is within bounds.
# If one string is longer, continue appending its remaining characters.
# Join the result into a final string.
#
# Time: O(n + m)
# Space: O(n + m)


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr = []

        ptr1 = 0
        ptr2 = 0

        while ptr1 < len(word1) or ptr2 < len(word2):

            if ptr1 < len(word1):
                arr.append(word1[ptr1])
                ptr1 += 1

            if ptr2 < len(word2):
                arr.append(word2[ptr2])
                ptr2 += 1

        return "".join(arr)
