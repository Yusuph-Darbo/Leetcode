# Approach:
# Use a monotonic decreasing stack to keep track of indices
# whose next warmer temperature has not been found yet.
# When a warmer temperature is found, calculate the distance
# between the current index and the stored index.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)

        return res
