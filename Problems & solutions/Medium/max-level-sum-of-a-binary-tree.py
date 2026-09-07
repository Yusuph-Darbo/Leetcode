# Approach:
# Perform a level-order traversal (BFS), computing the sum of node values
# at each level. Track the maximum level sum seen so far and return the
# level where it occurs.
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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        res = 0
        level = 1
        maxSum = float("-inf")

        while q:
            qLen = len(q)
            curr = 0

            for _ in range(qLen):
                node = q.popleft()
                curr += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if curr > maxSum:
                res = level
                maxSum = curr

            level += 1

        return res
