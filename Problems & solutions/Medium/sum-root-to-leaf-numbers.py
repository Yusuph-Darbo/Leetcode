# Approach:
# Use DFS to traverse every root-to-leaf path while building the number
# incrementally. At each node, multiply the current number by 10 and add
# the node's value. When reaching a leaf, return the completed number.
# Sum the results from the left and right subtrees.
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
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(node, path):
            if not node:
                return 0

            path = path * 10 + node.val

            if not node.left and not node.right:
                return path

            return dfs(node.left, path) + dfs(node.right, path)

        return dfs(root, 0)
