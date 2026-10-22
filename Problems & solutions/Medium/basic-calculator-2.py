# Approach:
# Use a single pass to parse numbers and track the previous term. Addition
# and subtraction update the running result directly, while multiplication
# and division replace the previous term to respect operator precedence.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def calculate(self, s: str) -> int:
        prev = cur = res = 0
        operation = "+"
        i = 0

        while i < len(s):
            cur_char = s[i]

            if cur_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1

                i -= 1

                if operation == "+":
                    res += cur
                    prev = cur

                elif operation == "-":
                    res -= cur
                    prev = -cur

                elif operation == "*":
                    res -= prev
                    res += cur * prev

                    prev = prev * cur

                else:
                    res -= prev
                    res += int(prev / cur)

                    prev = int(prev / cur)

                cur = 0

            elif cur_char != " ":
                operation = cur_char

            i += 1

        return res
