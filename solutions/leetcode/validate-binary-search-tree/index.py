from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: TreeNode, lb: int, ub: int):
            if not node:
                return True
            if not (lb < node.val and node.val < ub):
                return False

            return (dfs(node.left, lb, node.val) and
                    dfs(node.right, node.val, ub))

        return dfs(root, float('-inf'), float('inf'))


# Iterative
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, float("-inf"), float("inf"))]

        while stack:
            node, left, right = stack.pop()

            if not (left < node.val < right):
                return False

            if node.left:
                stack.append((node.left, left, node.val))
            if node.right:
                stack.append((node.right, node.val, right))

        return True
