from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node: Optional[TreeNode]):
            if not node or node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            elif left:
                return left
            elif right:
                return right
            return None

        return dfs(root)
