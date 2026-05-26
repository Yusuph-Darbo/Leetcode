# Approach:
# Store all characters in a set for fast lookups.
# For each letter from a to z, check whether both
# its lowercase and uppercase forms exist in the word.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        sett = set(word)
        count = 0

        for i in range(26):
            lower = chr(ord("a") + i)
            upper = chr(ord("A") + i)

            if lower in sett and upper in sett:
                count += 1

        return count
