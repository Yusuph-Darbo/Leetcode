# Approach:
# Use DFS to calculate the height of each subtree.
# At every node, compute the diameter as left height + right height.
# Track the maximum diameter found during traversal.
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Instance variable
        self.res = 0

        def dfs(curr):
            if curr == None:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.res
