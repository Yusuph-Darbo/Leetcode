# Approach:
# Count the frequency of each letter using fixed-size arrays. First, verify
# that both strings contain the same set of characters. Then sort the
# frequency arrays and compare them to check if the character frequencies
# can be rearranged to match.
#
# Time: O(n + m)
# Space: O(1)


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26

        for c in word1:
            freq1[ord(c) - ord("a")] += 1

        for c in word2:
            freq2[ord(c) - ord("a")] += 1

        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False

        freq1.sort()
        freq2.sort()

        for i in range(26):
            if freq1[i] != freq2[i]:
                return False

        return True
