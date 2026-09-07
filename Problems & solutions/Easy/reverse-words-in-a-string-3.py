# Approach:
# Convert the string to a list and reverse each word in place by swapping
# characters from both ends. Join the characters back together at the end.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        length = len(chars)

        start = 0

        for end in range(length + 1):
            if end == length or chars[end] == " ":
                left, right = start, end - 1
                while left < right:
                    chars[left], chars[right] = chars[right], chars[left]
                    left += 1
                    right -= 1

                start = end + 1

        return "".join(chars)
