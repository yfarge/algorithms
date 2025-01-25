from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node: Optional[TreeNode]):
            if not node:
                return None

            leftTail = dfs(node.left)
            rightTail = dfs(node.right)

            if leftTail:
                leftTail.right = node.right
                node.right = node.left
                node.left = None

            return rightTail or leftTail or node

        dfs(root)


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preorder(node: Optional[TreeNode]):
            if not node:
                return []

            return [node] + preorder(node.left) + preorder(node.right)

        nodes = preorder(root)
        for i in range(1, len(nodes)):
            nodes[i - 1].left = None
            nodes[i - 1].right = nodes[i]
