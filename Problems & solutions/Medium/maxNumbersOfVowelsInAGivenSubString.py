# Approach:
# Use a sliding window of size k over s.
# Count vowels in the window and update the max count.
# As the window moves, add the new char and remove the old one.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        left, right, count, maxCount = 0, 0, 0, 0

        for right in range(len(s)):
            if s[right] in vowels:
                count += 1

            if right - left + 1 == k:
                maxCount = max(maxCount, count)

                if s[left] in vowels:
                    count -= 1
                left += 1

        return maxCount
