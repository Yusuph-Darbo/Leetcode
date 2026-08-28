# Approach:
# Build the graph one edge at a time. Before adding an edge, use DFS to
# check if its two nodes are already connected. If they are, the edge is
# redundant; otherwise, add it to the graph.
#
# Time: O(e * (v + e))
# Space: O(v)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(node, target, visit):
            if node == target:
                return True

            visit.add(node)

            for nei in graph[node]:
                if nei not in visit:
                    if dfs(nei, target, visit):
                        return True

            return False

        for v, e in edges:
            if dfs(v, e, set()):
                return [v, e]

            graph[v].append(e)
            graph[e].append(v)

        return []
