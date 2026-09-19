# Approach:
# Rotate the matrix in-place by moving four cells at a time. For each position,
# save the four values, then shift them clockwise into their new positions.
#
# Time: O(n^2)
# Space: O(1)


class Solution:
    def rotate(self, mat: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(mat)
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                a = mat[i][j]
                b = mat[j][n - 1 - i]
                c = mat[n - 1 - i][n - 1 - j]
                d = mat[n - j - 1][i]

                mat[i][j] = d
                mat[j][n - 1 - i] = a
                mat[n - 1 - i][n - 1 - j] = b
                mat[n - j - 1][i] = c
