# Approach:
# Treat the matrix as a graph where each city is a node and a connection
# represents an edge. Use DFS to visit every connected city. Each new DFS
# traversal starts a new province.
#
# Time: O(n^2)
# Space: O(n)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        provinces = 0

        def dfs(city):
            seen.add(city)

            for cur, connected in enumerate(isConnected[city]):
                if connected and cur not in seen:
                    dfs(cur)

        for i in range(len(isConnected)):
            if i not in seen:
                dfs(i)
                provinces += 1

        return provinces
