# Approach:
# Use a sliding window with a set to track unique characters.
# Expand the right pointer; if a duplicate is found, shrink from the left until valid.
# Update the maximum window size at each step.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        sub = set()
        length = 0

        for right in range(len(s)):
            while s[right] in sub:
                sub.remove(s[left])
                left += 1

            sub.add(s[right])
            length = max(length, right - left + 1)

        return length
