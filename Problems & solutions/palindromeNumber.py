# Approach:
# Instead of reversing the entire number, only reverse half of it.
# Continue extracting digits until the reversed half is greater than or equal to the remaining half.
# For even-length numbers, the two halves should match exactly.
# For odd-length numbers, the middle digit can be ignored (reverse // 10).
#
# Time Complexity: O(log n) — we process about half the digits of x.
# Space Complexity: O(1) — only a few integer variables are used.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse = 0

        while x > reverse:
            reverse = reverse * 10 + (x % 10)
            x //= 10
        
        return x == reverse or x == reverse // 10
