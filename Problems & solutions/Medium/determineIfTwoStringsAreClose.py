# Approach:
# Count the frequency of each character in both strings. The strings are
# close if they contain the same set of characters and their character
# frequencies can be rearranged to match.
#
# Time: O(n + m)
# Space: O(n + m)


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        f1 = Counter(c1.values())
        f2 = Counter(c2.values())

        return f1 == f2 and set(word1) == set(word2)
