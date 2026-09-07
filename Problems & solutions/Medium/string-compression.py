# Approach:
# Use two pointers: one to iterate through the array and count consecutive characters,
# and another to write the compressed result in-place.
# For each group of repeating characters, write the character followed by its count (if > 1).
# Return the length of the compressed array.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        if length < 2:
            return length

        i = j = 0

        while i < length:
            count = 1
            while i < length - 1 and chars[i] == chars[i + 1]:
                count += 1
                i += 1

            chars[j] = chars[i]
            j += 1
            if count > 1:
                for val in str(count):
                    chars[j] = val
                    j += 1

            i += 1

        return j
