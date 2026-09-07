# Approach:
# Count the characters in both strings. For each target character, calculate
# how many complete copies can be formed and take the minimum.
#
# Time: O(n + m)
# Space: O(1)


class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        stringCount = Counter(s)
        targetWord = Counter(target)

        res = len(s)

        for c in targetWord:
            res = min(res, stringCount[c] // targetWord[c])

        return res
