# Approach:
# Use DFS to search for p and q. If a node finds one target in each subtree,
# it is their lowest common ancestor. Otherwise, propagate the found target
# upward until both targets meet.
#
# Time: O(n)
# Space: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        def dfs(node):
            if not node or node == q or node == p:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node

            return left or right

        return dfs(root)
