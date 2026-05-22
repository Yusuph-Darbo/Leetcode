# Approach:
# Use four pointers (top, bottom, left, right) to define the current layer.
# Traverse in four directions: left ->right, top -> bottom, right -> left, bottom -> top.
# After each pass, shrink the boundaries inward.
# Repeat until all elements are visited.

# Time: O(m * n)
# Space: O(1) (excluding output)


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while left <= right and top <= bottom:

            # Traverse top row
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # Traverse right column
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # Traverse bottom row (if still valid)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # Traverse left column (if still valid)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res
