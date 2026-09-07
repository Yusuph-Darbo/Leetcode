# Approach:
# Use Counter to count the frequency of each character in the input string.
# Also use Counter to count the frequency of each character required to form the word "balloon".
#
# The number of times "balloon" can be formed depends on the limiting character.
# For each character in "balloon", divide its frequency in the input string
# by its required frequency in "balloon".
#
# The minimum result among these values determines the maximum number of times
# the word "balloon" can be formed.
#
# Return this minimum value.
#
# Time Complexity: O(n) — counting characters requires one pass through the string.
# Space Complexity: O(1) — limited extra space since alphabet size is constant.

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # Counter returns each unique character and the num of occuriences 
        textCount = Counter(text)
        balloon = Counter("balloon")

        # Cannot create ballon more times than the amount of letters
        res = len(text)

        for c in balloon:
            # Finds the minimun amount of characters needed to create balloon
            res = min(res, textCount[c] // balloon[c])

        return res
        