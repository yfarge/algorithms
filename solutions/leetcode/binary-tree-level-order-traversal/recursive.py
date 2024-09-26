from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node: Optional[TreeNode], level: int):
            if not node:
                return

            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        levels = []
        dfs(root, 0)
        return levels
