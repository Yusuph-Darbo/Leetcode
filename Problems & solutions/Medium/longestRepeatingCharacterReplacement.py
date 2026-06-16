# Approach:
# Use a sliding window and track the frequency of characters within the
# window. If the number of characters that must be replaced to make the
# entire window consist of the most frequent character exceeds k, shrink
# the window from the left. Keep track of the largest valid window seen.
#
# Time: O(26 * n) ≈ O(n)
# Space: O(1)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res
