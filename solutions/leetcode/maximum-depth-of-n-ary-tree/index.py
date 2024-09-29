from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


# Recursive
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node: 'Node'):
            if not node.children:
                return 1

            depth = 0
            for child in node.children:
                depth = max(depth, 1 + dfs(child))

            return depth

        if not root:
            return 0

        return dfs(root)


# Iterative
class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:
            return 0

        stack = [(1, root)]
        depth = 0
        while stack:
            current_depth, node = stack.pop()
            depth = max(depth, current_depth)
            for child in node.children:
                stack.append((current_depth + 1, child))

        return depth
