# Approach:
# Build an undirected graph and use DFS to detect cycles while tracking the
# previous node. A valid tree must have no cycles and all n nodes must be
# connected.
#
# Time: O(v + e)
# Space: O(v + e)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for v, e in edges:
            graph[v].append(e)
            graph[e].append(v)

        seen = set()
        def dfs(node, prev):
            if node in seen:
                return False

            seen.add(node)
            for nei in graph[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        return dfs(0, -1) and len(seen) == n