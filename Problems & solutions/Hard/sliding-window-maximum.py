# Approach:
# Use a monotonic decreasing deque to store indices of potential maximums.
# Remove smaller elements from the back, discard indices outside the window
# from the front, and record the front element as the maximum for each window.
#
# Time: O(n)
# Space: O(k)


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        queue = deque()
        l = r = 0
        res = []

        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            queue.append(r)

            if l > queue[0]:
                queue.popleft()

            if (r + 1) >= k:
                res.append(nums[queue[0]])
                l += 1

            r += 1

        return res
