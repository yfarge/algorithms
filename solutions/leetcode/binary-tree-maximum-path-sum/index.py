from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')

        def dfs(node: Optional[TreeNode]):
            nonlocal result
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            result = max(result, node.val + left + right)
            return max(node.val + left, node.val + right, 0)

        dfs(root)
        return result
