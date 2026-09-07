# Approach:
# Traverse the tree while recording the parent and depth of the two target
# nodes. The nodes are cousins if they have different parents but are found
# at the same depth.
#
# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res = []

        def bfs(node, parent, depth):
            if not node:
                return

            if node.val == x or node.val == y:
                res.append((parent, depth))

            bfs(node.left, node, depth + 1)
            bfs(node.right, node, depth + 1)

        bfs(root, None, 0)
        l, r = res

        return l[0] != r[0] and l[1] == r[1]
