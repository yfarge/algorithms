# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        stack = [(root, root.val)]
        while stack:
            node, current_max = stack.pop()
            if node.val >= current_max:
                result += 1
            if node.left:
                stack.append((node.left, max(current_max, node.val)))
            if node.right:
                stack.append((node.right, max(current_max, node.val)))
        return result
