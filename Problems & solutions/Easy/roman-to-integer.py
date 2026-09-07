# Approach:
# Map each Roman numeral to its value. Subtract a numeral when it is smaller
# than the next one; otherwise, add it to the total.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        value = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman_int[s[i]] < roman_int[s[i + 1]]:
                value -= roman_int[s[i]]
            else:
                value += roman_int[s[i]]

        return value
