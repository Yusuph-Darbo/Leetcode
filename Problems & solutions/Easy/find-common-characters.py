# Approach:
# Count the frequency of characters in the first word, then intersect it
# with the frequency count of each remaining word. The remaining character
# counts represent the characters common to every word.
#
# Time: O(n * m)
# Space: O(1)


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = Counter(words[0])

        for word in words:
            # AND operator
            freq &= Counter(word)

        return list(freq.elements())
