# Approach:
# Use BFS to clone each node while storing a mapping from original nodes to
# their copies. For each node, connect its clone to the clones of its
# neighbors using the mapping.
#
# Time: O(v + t)
# Space: O(v)

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)

                oldToNew[cur].neighbors.append(oldToNew[nei])

        return oldToNew[node]
