# Approach:
# Remove dashes and convert all characters to uppercase. Then split the
# characters into groups of size k from the end and join them with dashes.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        # Iterate through the string and collect all chars

        arr = []

        for char in s:
            if char != "-":
                arr.append(char.upper())

        groups = []

        i = len(arr)

        while i > 0:
            groups.append("".join(arr[max(0, i - k) : i]))
            i -= k

        groups.reverse()
        return "-".join(groups)
