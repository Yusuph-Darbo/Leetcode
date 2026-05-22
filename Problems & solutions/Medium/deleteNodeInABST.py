# Approach:
# Traverse the BST recursively to find the node with the target key.
# If the node has one or no children, replace it directly.
# If the node has two children, replace its value with the
# smallest value in the right subtree, then delete that node.
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return root

        if key == root.val:
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            root.left = self.deleteNode(root.left, key)

        return root
