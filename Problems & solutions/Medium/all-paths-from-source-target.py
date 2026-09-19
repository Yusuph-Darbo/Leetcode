# Approach:
# Use DFS with backtracking to explore every path from node 0 to node n - 1.
# Add the current node to the path, save a copy when the target is reached,
# then remove it while backtracking.
#
# Time: Exponential
# Space: O(n)


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        mapp = {}
        for i in range(len(graph)):
            mapp[i] = graph[i]

        n = len(graph)
        res = []

        def dfs(node, path):
            path.append(node)

            if node == n - 1:
                res.append(path.copy())
                path.pop()
                return

            for nei in mapp[node]:
                dfs(nei, path)

            path.pop()

        dfs(0, [])

        return res
