# Approach:
# Use BFS to traverse the matrix diagonally. Start from the top-left cell,
# enqueue the first element of the next row when visiting the first column,
# and enqueue the next element in the current row to process elements in
# diagonal order.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        q = deque([(0, 0)])

        while q:
            row, col = q.popleft()
            res.append(nums[row][col])

            if col == 0 and row + 1 < len(nums):
                q.append((row + 1, col))

            if col + 1 < len(nums[row]):
                q.append((row, col + 1))

        return res
