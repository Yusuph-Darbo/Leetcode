# Approach:
# Use a sliding window of size len(s1) to scan through s2.
# Maintain two frequency arrays: one for s1 and one for the current window in s2.
# Initialize both counts for the first window.
# Slide the window across s2, updating counts by removing the left char and adding the new right char.
# At each step, compare the two frequency arrays; if they match, a permutation exists, so return True.
# If no match is found, return False.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        # Count each occurrence
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        for i in range(len(s2) - len(s1) + 1):
            if s1Count == s2Count:
                return True

            # Move window
            if i + len(s1) < len(s2):
                # Remove last char
                s2Count[ord(s2[i]) - ord("a")] -= 1
                s2Count[ord(s2[i + len(s1)]) - ord("a")] += 1

        return False
