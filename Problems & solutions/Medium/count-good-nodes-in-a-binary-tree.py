# Approach:
# Use depth-first search while tracking the maximum value
# seen on the path from the root to the current node.
# A node is good if its value is greater than or equal to
# the maximum value encountered so far.
#
# Time: O(n)
# Space: O(h)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        return dfs(root, root.val)
