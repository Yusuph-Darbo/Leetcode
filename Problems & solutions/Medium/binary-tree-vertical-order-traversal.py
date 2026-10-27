# Approach:
# Use BFS to traverse the tree level by level, assigning each node a column
# index. The left child is at col - 1 and the right child at col + 1.
# Group node values by column, then return columns from left to right.
#
# Time: O(n)
# Space: O(n)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    def vertical_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        min_col = max_col = 0
        q = deque([(root, 0)])
        cols = defaultdict(list)

        while q:
            node, col = q.popleft()

            min_col = min(min_col, col)
            max_col = max(max_col, col)

            cols[col].append(node.val)

            if node.left:
                q.append((node.left, col - 1))

            if node.right:
                q.append((node.right, col + 1))

        return [cols[c] for c in range(min_col, max_col + 1)]
