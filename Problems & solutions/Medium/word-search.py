# Approach:
# Use DFS with backtracking to search for the word from each possible starting
# cell. Track visited cells to prevent reusing the same cell in one path.
#
# Time: O(m * n * 4^L)
# Space: O(L)


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()

        def dfs(x, y, length):
            if length == len(word):
                return True

            if (
                x < 0
                or y < 0
                or x >= rows
                or y >= cols
                or (x, y) in seen
                or board[x][y] != word[length]
            ):
                return False

            seen.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if dfs(nx, ny, length + 1):
                    return True

            seen.remove((x, y))
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in word:
                    if dfs(r, c, 0):
                        return True

        return False
