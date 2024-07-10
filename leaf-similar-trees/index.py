from typing import Optional
from itertools import zip_longest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode):
            if node:
                if node.left is None and node.right is None:
                    yield node.val

                yield from dfs(node.left)
                yield from dfs(node.right)

        return all(a == b for a, b in zip_longest(dfs(root1), dfs(root2)))
