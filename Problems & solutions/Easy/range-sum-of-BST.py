# Approach:
# Use iterative DFS with a stack to traverse the BST. Add each node's value
# if it falls within the range [low, high]. Push its children onto the stack
# to continue exploring the tree.
#
# Time: O(n)
# Space: O(h) average, O(n) worst case


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        result = 0

        stack = [root]

        while stack:
            node = stack.pop()

            if low <= node.val <= high:
                result += node.val

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result
