# Approach:
# Start from the top-right corner of the matrix.
# Move left if the current element is greater than the target.
# Move down if the current element is less than the target.
# Continue until the target is found or bounds are exceeded.
#
# Time: O(m + n)
# Space: O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        ele = len(matrix[0]) - 1

        while row < len(matrix) and ele >= 0:
            if matrix[row][ele] == target:
                return True
            elif matrix[row][ele] < target:
                row += 1
            else:
                ele -= 1

        return False
