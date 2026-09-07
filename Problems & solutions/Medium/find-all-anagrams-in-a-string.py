# Approach:
# Use a sliding window of size len(p) to scan through s.
# Maintain two frequency arrays: one for p and one for the current window in s.
# Initialize both counts for the first window.
# Slide the window across s, updating counts by removing the left char and adding the new right char.
# At each step, compare the two frequency arrays; if they match, record the starting index.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len(s):
            return res

        pCount = [0] * 26
        sCount = [0] * 26

        for i in range(len(p)):
            pCount[ord(p[i]) - ord("a")] += 1
            sCount[ord(s[i]) - ord("a")] += 1

        for i in range(len(s) - len(p) + 1):
            if pCount == sCount:
                res.append(i)

            # Move window
            if i + len(p) < len(s):
                # Remove old char
                sCount[ord(s[i]) - ord("a")] -= 1
                # Add new char
                sCount[ord(s[i + len(p)]) - ord("a")] += 1

        return res
