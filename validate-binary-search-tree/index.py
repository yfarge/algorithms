from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: TreeNode, lb, ub):
            if node == None:
                return True
            if not (lb < node.val and node.val < ub):
                return False

            return(dfs(node.left, lb, node.val) and
                   dfs(node.right, node.val, ub))

        return dfs(root, float('-inf'), float('inf'))
