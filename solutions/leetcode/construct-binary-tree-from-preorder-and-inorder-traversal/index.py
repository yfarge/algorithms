from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(left: int, right: int):
            nonlocal preorder_index
            if right < left:
                return None

            root = TreeNode(preorder[preorder_index])
            inorder_index = inorder_index_map[root.val]

            preorder_index += 1

            root.left = dfs(left, inorder_index - 1)
            root.right = dfs(inorder_index + 1, right)

            return root

        preorder_index = 0
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return dfs(0, len(preorder) - 1)
