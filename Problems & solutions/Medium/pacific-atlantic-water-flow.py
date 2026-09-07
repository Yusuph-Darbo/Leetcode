# Approach:
# Run DFS from each ocean's borders, moving only to cells with equal or
# greater height. Cells reachable from both oceans can flow to both.
#
# Time: O(m * n)
# Space: O(m * n)


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pac, atl = set(), set()
        res = []

        def dfs(r, c, visit, prevHeight):
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or (r, c) in visit
                or heights[r][c] < prevHeight
            ):
                return

            visit.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visit, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl and (r, c) in pac:
                    res.append((r, c))

        return res
