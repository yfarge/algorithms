from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(lTree: TreeNode, rTree: TreeNode):
            if (not lTree and not rTree):
                return True
            if (not lTree or not rTree or lTree.val != rTree.val):
                return False
            return (dfs(lTree.left, rTree.right) and dfs(lTree.right, rTree.left))

        return dfs(root.left, root.right)
