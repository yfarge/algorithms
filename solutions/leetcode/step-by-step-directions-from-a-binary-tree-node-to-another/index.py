from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lca(self, root: Optional[TreeNode], s: int, d: int) -> Optional[TreeNode]:
        if not root:
            return root

        if root.val == s or root.val == d:
            return root

        left = self.lca(root.left, s, d)
        right = self.lca(root.right, s, d)

        if not left:
            return right
        elif not right:
            return left
        return root

    def findPath(self, root: TreeNode, value: int, path: List[str]) -> bool:
        if not root:
            return False

        if root.val == value:
            return True

        path.append("L")
        if self.findPath(root.left, value, path):
            return True
        path.pop()

        path.append("R")
        if self.findPath(root.right, value, path):
            return True
        path.pop()

        return False

    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        lca = self.lca(root, startValue, destValue)
        lca_to_start, lca_to_dest = [], []

        self.findPath(lca, startValue, lca_to_start)
        self.findPath(lca, destValue, lca_to_dest)

        for i in range(len(lca_to_start)):
            lca_to_start[i] = "U"

        return "".join(lca_to_start + lca_to_dest)
