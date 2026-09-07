# Approach:
# Use DFS to compute the height of each subtree.
# A node is balanced if both subtrees are balanced and their heights differ by at most 1.
# Return both the balance status and subtree height during traversal.
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(curr):
            if curr == None:
                return [True, 0]

            l = dfs(curr.left)
            r = dfs(curr.right)

            balanced = l[0] and r[0] and abs(l[1] - r[1]) <= 1

            return [balanced, 1 + max(l[1], r[1])]

        return dfs(root)[0]
