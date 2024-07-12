from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0, 0)]
        max_count = 0

        while stack:
            node, dir, count = stack.pop()

            if count > max_count:
                max_count = count

            if node.left:
                stack.append((node.left, -1, count + 1 if dir >= 0 else 1))

            if node.right:
                stack.append((node.right, 1, count + 1 if dir <= 0 else 1))

        return max_count
