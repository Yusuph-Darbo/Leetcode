# Approach:
# Iterate from 1 to n and check whether each number is divisible by 3, 5,
# both, or neither, adding the appropriate value to the result.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        Value = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                Value.append("FizzBuzz")
            elif i % 5 == 0:
                Value.append("Buzz")
            elif i % 3 == 0:
                Value.append("Fizz")
            else:
                Value.append(str(i))

        return Value
