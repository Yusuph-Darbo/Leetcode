# Approach:
# Recursively traverse the BST using its ordering property. If the target
# value is smaller than the current node, search the left subtree; if larger,
# search the right subtree. Return the node when found, or None if the value
# does not exist in the tree.
#
# Time: O(h)
# Space: O(h)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
