# Approach:
# Traverse the matrix diagonally, alternating between upward and downward
# directions. Adjust the row and column when reaching a boundary.
#
# Time: O(m * n)
# Space: O(m * n)


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        res = []

        curRow = curCol = 0
        goingUp = True

        while len(res) != (rows * cols):
            if goingUp:
                while curRow >= 0 and curCol < cols:
                    res.append(mat[curRow][curCol])

                    curRow -= 1
                    curCol += 1

                if curCol == cols:
                    curRow += 2
                    curCol -= 1
                else:
                    curRow += 1

                goingUp = False

            else:
                while curRow < rows and curCol >= 0:
                    res.append(mat[curRow][curCol])

                    curRow += 1
                    curCol -= 1

                if curRow == rows:
                    curCol += 2
                    curRow -= 1
                else:
                    curCol += 1

                goingUp = True

        return res
