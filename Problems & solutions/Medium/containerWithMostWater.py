# Approach:
# Use two pointers starting at the left and right ends of the array.
# Compute the area using the shorter height and the width between pointers,
# update the maximum area, and move the pointer at the shorter height inward.
#
# Time: O(n)
# Space: O(1)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right_ptr = len(height) - 1
        left_ptr = 0
        total = 0

        while left_ptr < right_ptr:
            width = right_ptr - left_ptr
            lower_tower = min(height[left_ptr], height[right_ptr])

            water = width * lower_tower

            total = max(total, water)

            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1

            else:
                right_ptr -= 1

        return total