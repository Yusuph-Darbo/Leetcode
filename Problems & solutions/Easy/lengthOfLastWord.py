# Approach:
# Start from the end of the string, skip trailing spaces, then move backwards
# until a space is found. The distance between these positions is the length
# of the last word.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1

        while s[end] == " ":
            end -= 1

        start = end

        while start >= 0 and s[start] != " ":
            start -= 1

        return end - start
