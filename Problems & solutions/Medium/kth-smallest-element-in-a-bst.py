# Approach:
# Perform an inorder traversal iteratively using a stack.
# Since inorder traversal of a BST visits nodes in sorted order,
# store the values and return the k-th smallest element.
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            arr.append(curr.val)
            curr = curr.right

        return arr[k - 1]
