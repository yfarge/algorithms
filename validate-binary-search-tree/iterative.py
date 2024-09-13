from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
