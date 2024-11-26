from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        currentSum = targetSum - root.val
        if not root.left and not root.right:
            return currentSum == 0

        left = self.hasPathSum(root.left, currentSum)
        right = self.hasPathSum(root.right, currentSum)

        return left or right
