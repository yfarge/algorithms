from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]):
            nonlocal is_balanced
            if not node:
                return 0

            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)

            if abs(left - right) > 1:
                is_balanced = False

            return max(left, right)

        if not root:
            return True

        is_balanced = True
        dfs(root)
        return is_balanced
