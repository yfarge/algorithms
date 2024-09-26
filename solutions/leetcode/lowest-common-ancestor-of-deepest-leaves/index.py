from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDepth(self, node: Optional[TreeNode], depth: int):
        if not node:
            return depth - 1

        left_depth = self.getDepth(node.left, depth + 1)
        right_depth = self.getDepth(node.right, depth + 1)

        return max(left_depth, right_depth)

    def lca(self, node: Optional[TreeNode], depth: int, target: int):
        if not node:
            return node

        if depth == target:
            return node

        left = self.lca(node.left, depth + 1, target)
        right = self.lca(node.right, depth + 1, target)

        if left and right:
            return node
        elif left:
            return left
        elif right:
            return right
        return None

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.lca(root, 0, self.getDepth(root, 0))
