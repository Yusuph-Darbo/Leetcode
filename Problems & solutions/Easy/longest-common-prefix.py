# Approach:
# Compare each character across all strings. Stop when a character differs
# or a string ends, otherwise add it to the common prefix.
#
# Time: O(n * m)
# Space: O(1)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]

        return prefix
