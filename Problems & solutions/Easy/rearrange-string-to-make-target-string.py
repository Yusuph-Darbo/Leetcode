
# Approach:
# Use Counter to count the frequency of each character in the string s.
# Also use Counter to count the frequency of each character required to form the target string.
#
# The number of times the target can be formed depends on the character
# that appears the fewest number of complete times.
#
# For each character in the target, divide its frequency in s
# by its required frequency in the target.
#
# The minimum value among these results determines the maximum number
# of times the target string can be formed.
#
# Return this minimum value.
#
# Time Complexity: O(n + m) — where n is length of s and m is length of target.
# Space Complexity: O(1) — extra space is constant since alphabet size is limited.


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
        