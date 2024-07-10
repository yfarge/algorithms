from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        queue = deque([(root, root.val)])
        while queue:
            node, current_max = queue.popleft()
            if node.val >= current_max:
                result += 1
            if node.left:
                queue.append((node.left, max(current_max, node.val)))
            if node.right:
                queue.append((node.right, max(current_max, node.val)))
        return result
