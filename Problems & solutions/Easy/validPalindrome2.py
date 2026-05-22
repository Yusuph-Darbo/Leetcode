# Approach:
# Use two pointers to compare characters from both ends.
# If a mismatch is found, try skipping either the left or right character.
# Check if either remaining substring is a palindrome.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(arr):
            l, r = 0, len(arr) - 1

            while l < r:
                if arr[l] != arr[r]:
                    return False
                l += 1
                r -= 1

            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL = s[l + 1 : r + 1]
                skipR = s[l:r]

                return isPalindrome(skipL) or isPalindrome(skipR)

            l += 1
            r -= 1

        return True
