# Approach:
# Use a monotonic increasing stack to find the previous smaller element.
# For each value, calculate how many subarrays use it as the minimum and add
# its contribution to the result.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        stack = []
        res = [0] * len(arr)

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            j = stack[-1] if stack else -1
            res[i] = res[j] + (i - j) * arr[i]

            stack.append(i)

        return sum(res) % (10**9 + 7)
